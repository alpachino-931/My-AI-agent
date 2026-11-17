"""Эмбеддинги для Дня 19.

Основной путь — Sentence Transformers с мультиязычной моделью.
Если библиотека или модель не подготовлены на учебном ПК, используется
резервный учебный эмбеддер на хешах слов и символьных n-грамм. Он не
заменяет нейросетевую модель по качеству, но позволяет отработать весь
алгоритм: encode → similarity → поиск лучшего чанка.
"""

import csv
import hashlib
import re
import sys
from pathlib import Path

import numpy as np

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
FALLBACK_DIMENSION = 2048

_WORD_RE = re.compile(r"[a-zа-я0-9]+", re.IGNORECASE)


class HashEmbedder:
    """Учебный эмбеддер: слова и символьные n-граммы, хешированные в вектор."""

    def __init__(self, dimension: int = FALLBACK_DIMENSION) -> None:
        self.dimension = dimension

    @staticmethod
    def _features(text: str) -> dict[str, float]:
        text = text.lower().replace("ё", "е")
        features: dict[str, float] = {}

        for token in _WORD_RE.findall(text):
            key = "w:" + token
            features[key] = features.get(key, 0.0) + 1.0

            padded = f"<{token}>"
            for size in (3, 4):
                for start in range(len(padded) - size + 1):
                    gram = f"c{size}:" + padded[start:start + size]
                    features[gram] = features.get(gram, 0.0) + 0.4

        return features

    def _embed_one(self, text: str) -> np.ndarray:
        vector = np.zeros(self.dimension, dtype=np.float32)
        for feature, value in self._features(text).items():
            digest = hashlib.md5(feature.encode("utf-8")).digest()
            index = int.from_bytes(digest[:4], "little") % self.dimension
            sign = 1.0 if digest[4] & 1 else -1.0
            vector[index] += value * sign

        norm = float(np.linalg.norm(vector))
        if norm > 0:
            vector /= norm
        return vector

    def encode(self, texts, **kwargs):
        """Повторяет поведение SentenceTransformer.encode()."""
        if isinstance(texts, str):
            return self._embed_one(texts)

        vectors = [self._embed_one(text) for text in texts]
        if not vectors:
            return np.zeros((0, self.dimension), dtype=np.float32)
        return np.vstack(vectors)


class Embedder:
    """Единый интерфейс для настоящей модели и резервного эмбеддера."""

    def __init__(self, backend, name: str, is_fallback: bool = False) -> None:
        self.backend = backend
        self.name = name
        self.is_fallback = is_fallback

    def encode(self, texts):
        return self.backend.encode(texts)

    @staticmethod
    def similarity(left, right) -> np.ndarray:
        """Косинусное сходство: косинус угла между векторами."""
        left = np.atleast_2d(np.asarray(left, dtype=np.float64))
        right = np.atleast_2d(np.asarray(right, dtype=np.float64))

        left_norm = np.linalg.norm(left, axis=1, keepdims=True)
        right_norm = np.linalg.norm(right, axis=1, keepdims=True)
        left = left / np.where(left_norm == 0, 1.0, left_norm)
        right = right / np.where(right_norm == 0, 1.0, right_norm)
        return left @ right.T

    @property
    def dimension(self) -> int:
        if hasattr(self.backend, "get_sentence_embedding_dimension"):
            return int(self.backend.get_sentence_embedding_dimension())
        return int(self.backend.dimension)


def load_embedder(verbose: bool = True) -> Embedder:
    """Загружает SentenceTransformer, а при недоступности — резервный вариант."""
    try:
        from sentence_transformers import SentenceTransformer

        model = SentenceTransformer(MODEL_NAME)
        if verbose:
            print("Embedding-модель:", MODEL_NAME)
        return Embedder(model, MODEL_NAME)
    except Exception as error:  # библиотека или модель не подготовлены
        if verbose:
            print("Sentence Transformers недоступна:", type(error).__name__)
            print(f"Используется резервный учебный эмбеддер ({FALLBACK_DIMENSION} чисел).")
            print("Алгоритм поиска тот же: encode → similarity → лучший чанк.")
        return Embedder(
            HashEmbedder(FALLBACK_DIMENSION),
            f"hash-embedder ({FALLBACK_DIMENSION})",
            is_fallback=True,
        )


def cosine_similarity(vector_a, vector_b) -> float:
    """Косинусное сходство двух обычных векторов одинаковой длины."""
    return float(Embedder.similarity(vector_a, vector_b)[0][0])


def load_chunks(chunks_dir: str = "chunks", summary_file: str = "chunks_summary.csv") -> list[dict]:
    """Читает чанки Дня 18 по CSV-сводке source / chunk_id / length."""
    chunks_path = Path(chunks_dir)
    summary_path = Path(summary_file)

    chunks = []
    if summary_path.exists():
        with open(summary_path, encoding="utf-8", newline="") as source:
            for row in csv.DictReader(source):
                stem = Path(row["source"]).stem
                file_path = chunks_path / f"{stem}_chunk_{row['chunk_id']}.txt"
                text = file_path.read_text(encoding="utf-8")
                chunks.append({
                    "source": row["source"],
                    "chunk_id": int(row["chunk_id"]),
                    "length": len(text),
                    "text": text,
                })
        return chunks

    for file_path in sorted(chunks_path.glob("*.txt")):
        match = re.match(r"(.+)_chunk_(\d+)$", file_path.stem)
        if not match:
            continue
        text = file_path.read_text(encoding="utf-8")
        chunks.append({
            "source": match.group(1) + ".txt",
            "chunk_id": int(match.group(2)),
            "length": len(text),
            "text": text,
        })
    return chunks


def ask_questions(default_questions: list[str]) -> list[str]:
    """Спрашивает вопросы через input(); без терминала берёт готовые."""
    if not sys.stdin.isatty():
        print("Интерактивный ввод недоступен: используются готовые вопросы.")
        return list(default_questions)

    questions = []
    for number, default in enumerate(default_questions, start=1):
        try:
            answer = input(f"Вопрос {number} (Enter — «{default}»): ").strip()
        except (EOFError, KeyboardInterrupt):
            answer = ""
        questions.append(answer or default)
    return questions


def search(embedder: Embedder, chunks: list[dict], chunk_embeddings, question: str,
           top_k: int = 1) -> list[dict]:
    """Возвращает top_k чанков, отсортированных по убыванию сходства."""
    query_embedding = embedder.encode(question)
    scores = embedder.similarity(query_embedding, chunk_embeddings)[0].tolist()

    results = []
    for index, score in enumerate(scores):
        results.append({
            "index": index,
            "score": float(score),
            "source": chunks[index]["source"],
            "chunk_id": chunks[index]["chunk_id"],
            "text": chunks[index]["text"],
        })
    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:top_k]
