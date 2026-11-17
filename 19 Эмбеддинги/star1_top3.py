"""День 19, звёздочка 1: top-3 лучших чанка для каждого вопроса."""

import os

from embeddings import load_chunks, load_embedder, search

os.chdir(os.path.dirname(os.path.abspath(__file__)))

QUESTIONS = [
    "Почему возникает NameError?",
    "Как объявить функцию через def?",
    "Как создать список в Python?",
]


def main() -> None:
    embedder = load_embedder()
    chunks = load_chunks()
    chunk_embeddings = embedder.encode([chunk["text"] for chunk in chunks])

    for question in QUESTIONS:
        results = search(embedder, chunks, chunk_embeddings, question, top_k=3)
        print("\n" + "=" * 60)
        print("Вопрос:", question)
        for place, item in enumerate(results, start=1):
            print(f"\n{place}. score={round(item['score'], 4)}")
            print("   source:", item["source"])
            print("   chunk_id:", item["chunk_id"])
            print("   text:", item["text"][:100].replace("\n", " "))


if __name__ == "__main__":
    main()
