"""День 19, задания 14–18: вопрос и три чанка."""

import numpy as np

from embeddings import load_embedder

embedder = load_embedder()

print("--- Задание 14. Три чанка ---")
chunks = [
    "Списки Python создаются с помощью квадратных скобок.",
    "Git commit сохраняет изменения в истории.",
    "DataFrame — основная таблица Pandas.",
]
for index, chunk in enumerate(chunks):
    print(index, chunk)

print("\n--- Задание 15. Векторизация чанков ---")
chunk_embeddings = embedder.encode(chunks)
print("Форма:", chunk_embeddings.shape)

print("\n--- Задание 16. Вопрос ---")
query = "Как создать список?"
query_embedding = embedder.encode(query)
print("Вопрос:", query)
print("Размерность вектора вопроса:", len(query_embedding))

print("\n--- Задание 17. Scores ---")
scores = embedder.similarity(query_embedding, chunk_embeddings)
scores_list = scores[0].tolist()
for index, score in enumerate(scores_list):
    print(f"Чанк {index}: {round(score, 4)}")

print("\n--- Задание 18. Лучший результат ---")
best_score = max(scores_list)
best_index = scores_list.index(best_score)
print("Лучший индекс:", best_index)
print("Лучший чанк:", chunks[best_index])
print("Сходство:", round(best_score, 4))
print("Ожидался чанк про списки:", best_index == 0)
