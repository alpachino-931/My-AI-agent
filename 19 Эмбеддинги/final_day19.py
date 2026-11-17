"""День 19, задание 32: семантический поиск по чанкам.

Программа:
1. загружает минимум 10 чанков Дня 18 с source, chunk_id и text;
2. загружает одну embedding-модель;
3. считает embeddings всех чанков один раз;
4. получает вопросы через input() (без терминала — готовые вопросы);
5. считает similarity вопроса со всеми чанками;
6. находит лучший score и его индекс;
7. выводит source, chunk_id, текст и score с округлением;
8. повторяет поиск для пяти разных вопросов.
"""

import os
from pathlib import Path

from embeddings import ask_questions, load_chunks, load_embedder, search

os.chdir(os.path.dirname(os.path.abspath(__file__)))

DEFAULT_QUESTIONS = [
    "Почему возникает NameError?",
    "Как объявить функцию через def?",
    "Как открыть файл с помощью open()?",
    "Что делает list.append()?",
    "Как создать список в Python?",
]


def main() -> None:
    embedder = load_embedder()
    chunks = load_chunks()

    documents = {chunk["source"] for chunk in chunks}
    print("Документов:", len(documents))
    print("Чанков:", len(chunks))
    if len(chunks) < 10:
        print("Внимание: по методичке нужно минимум 10 чанков.")

    print("Модель:", embedder.name)
    print("Размерность embedding:", embedder.dimension)
    if embedder.is_fallback:
        print("Примечание: Sentence Transformers не установлена,")
        print("поэтому используется резервный учебный эмбеддер.")

    texts = []
    for chunk in chunks:
        texts.append(chunk["text"])

    chunk_embeddings = embedder.encode(texts)
    print("Форма матрицы embeddings:", chunk_embeddings.shape)

    questions = ask_questions(DEFAULT_QUESTIONS)
    for question in questions:
        best = search(embedder, chunks, chunk_embeddings, question)[0]

        print("\n" + "=" * 60)
        print("Вопрос:", question)
        print("source:", best["source"])
        print("chunk_id:", best["chunk_id"])
        print("score:", round(best["score"], 4))
        print("text:")
        print(best["text"])


if __name__ == "__main__":
    main()
