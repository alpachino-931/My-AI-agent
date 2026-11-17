"""День 19, задания 8–13: первый embedding и матрица сходств."""

import numpy as np

from embeddings import load_embedder

embedder = load_embedder()

print("--- Задание 8. Embedding одного предложения ---")
text = "Python — язык программирования"
embedding = embedder.encode(text)
print("Текст:", text)

print("\n--- Задание 9. Размерность ---")
print("Тип результата:", type(embedding).__name__)
print("len(embedding):", len(embedding))

print("\n--- Задание 10. Первые 10 чисел ---")
print("Первые 10 чисел:", np.round(embedding[:10], 4))
nonzero = np.nonzero(embedding)[0]
print("Ненулевых значений:", len(nonzero), "из", len(embedding))
print("Первый ненулевой индекс:", int(nonzero[0]))
print("Первые 10 ненулевых чисел:", np.round(embedding[nonzero[:10]], 4))

print("\n--- Задание 11. Три предложения ---")
texts = [
    "Как создать список в Python?",
    "Как работают списки Python?",
    "Какая сегодня погода?",
]
for index, item in enumerate(texts):
    print(index, item)

print("\n--- Задание 12. Матрица similarity ---")
embeddings = embedder.encode(texts)
print("Форма матрицы embeddings:", embeddings.shape)
similarities = embedder.similarity(embeddings, embeddings)
for row in similarities:
    print([round(float(value), 3) for value in row])

print("\n--- Задание 13. Сравнение ---")
close_score = float(similarities[0][1])
far_score = float(similarities[0][2])
print("Похожие тексты 0 и 1:", round(close_score, 3))
print("Разные тексты 0 и 2:", round(far_score, 3))
print("Более высокий score у пары 0–1:", close_score > far_score)
