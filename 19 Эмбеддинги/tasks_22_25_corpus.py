"""День 19, задания 22–25: поиск по корпусу чанков Дня 18."""

from embeddings import load_chunks, load_embedder, search

embedder = load_embedder()

print("--- Задание 22. Загрузка чанков ---")
chunks = load_chunks()
print("Загружено чанков:", len(chunks))
print("Документов:", len({chunk["source"] for chunk in chunks}))
for chunk in chunks[:3]:
    print(chunk["source"], chunk["chunk_id"], chunk["text"][:40].replace("\n", " "))

print("\n--- Задание 23. Embeddings всех чанков ---")
texts = []
for chunk in chunks:
    texts.append(chunk["text"])
chunk_embeddings = embedder.encode(texts)
print("Форма матрицы:", chunk_embeddings.shape)
print("Размерность одного вектора:", len(chunk_embeddings[0]))

print("\n--- Задания 24–25. Три вопроса и проверка источника ---")
questions = [
    "Почему возникает NameError?",
    "Как объявить функцию через def?",
    "Как открыть файл с помощью open()?",
]
for question in questions:
    best = search(embedder, chunks, chunk_embeddings, question)[0]
    print("\nВопрос:", question)
    print("source:", best["source"])
    print("chunk_id:", best["chunk_id"])
    print("score:", round(best["score"], 4))
    print("text:", best["text"][:120].replace("\n", " "))
