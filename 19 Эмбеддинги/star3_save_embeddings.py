"""День 19, звёздочка 3: сохранение embeddings в JSON-файл.

В файле embeddings.json лежит список объектов
{source, chunk_id, text, embedding}. Значения вектора округлены
до 6 знаков, чтобы файл оставался компактным.
"""

import json
import os
from pathlib import Path

from embeddings import load_chunks, load_embedder

os.chdir(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_FILE = Path("embeddings.json")


def main() -> None:
    embedder = load_embedder()
    chunks = load_chunks()
    chunk_embeddings = embedder.encode([chunk["text"] for chunk in chunks])

    records = []
    for index, chunk in enumerate(chunks):
        records.append({
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "text": chunk["text"],
            "embedding": [round(float(value), 6) for value in chunk_embeddings[index]],
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as output:
        json.dump(records, output, ensure_ascii=False)

    print("Сохранено чанков:", len(records))
    print("Размерность embedding:", len(records[0]["embedding"]))
    print("Файл:", OUTPUT_FILE.name, "| байт:", OUTPUT_FILE.stat().st_size)

    restored = json.loads(OUTPUT_FILE.read_text(encoding="utf-8"))
    required = {"source", "chunk_id", "text", "embedding"}
    print("Прочитано записей:", len(restored))
    print("Все поля на месте:", all(required <= set(item) for item in restored))
    print("Размерности совпадают:",
          all(len(item["embedding"]) == len(records[0]["embedding"]) for item in restored))


if __name__ == "__main__":
    main()
