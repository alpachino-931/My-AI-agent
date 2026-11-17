"""День 19, задания 26–29: исправление ошибок."""

from embeddings import load_embedder

embedder = load_embedder()

print("--- Задание 26. Ошибка вызова encode ---")
text = "Python — язык программирования"
try:
    wrong = embedder.encode[text]
except TypeError as error:
    print("Ошибка перехвачена:", error)
embedding = embedder.encode(text)
print("Правильный вызов, размерность:", len(embedding))

print("\n--- Задание 27. Ошибка индекса ---")
scores = [0.2, 0.8, 0.4]
best_score = max(scores)
try:
    best_index = best_score.index(scores)
except AttributeError as error:
    print("Ошибка перехвачена:", error)
best_index = scores.index(best_score)
print("best_score:", best_score)
print("best_index:", best_index)
print("chunk_index = best_index:", best_index)

print("\n--- Задание 28. Разные модели ---")
print("Чанки и вопрос должны быть закодированы одной моделью.")
print("У разных моделей свои размерности и своё векторное пространство,")
print("поэтому cosine similarity между ними теряет смысл.")

print("\n--- Задание 29. Ошибка метаданных ---")
chunks = [
    {"source": "python.txt", "chunk_id": 0},
    {"source": "git.txt", "chunk_id": 0},
]
try:
    print(chunks["source"])
except TypeError as error:
    print("Ошибка перехвачена:", error)
print("Правильно:", chunks[0]["source"])
