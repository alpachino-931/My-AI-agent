"""День 19, звёздочка 2: минимальный порог score.

Если лучший score ниже порога, программа сообщает, что подходящий
фрагмент не найден, вместо того чтобы выдавать случайный чанк.
"""

import os

from embeddings import load_chunks, load_embedder, search

os.chdir(os.path.dirname(os.path.abspath(__file__)))

THRESHOLD = 0.12
QUESTIONS = [
    "Почему возникает NameError?",
    "Как открыть файл?",
    "Какая завтра погода?",
]


def main() -> None:
    embedder = load_embedder()
    chunks = load_chunks()
    chunk_embeddings = embedder.encode([chunk["text"] for chunk in chunks])

    print("Порог:", THRESHOLD)
    for question in QUESTIONS:
        best = search(embedder, chunks, chunk_embeddings, question)[0]
        print("\nВопрос:", question)
        print("Лучший score:", round(best["score"], 4))
        if best["score"] < THRESHOLD:
            print("Подходящий фрагмент не найден")
            continue
        print("source:", best["source"])
        print("chunk_id:", best["chunk_id"])
        print("text:", best["text"][:100].replace("\n", " "))


if __name__ == "__main__":
    main()
