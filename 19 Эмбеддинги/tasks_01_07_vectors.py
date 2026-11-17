"""День 19, задания 1–7: вектор как список чисел и cosine similarity.

Библиотека scikit-learn на учебном ПК может быть не установлена, поэтому
косинусное сходство считается через numpy по той же формуле.
"""

from embeddings import cosine_similarity

print("--- Задание 1. Вектор из пяти чисел ---")
vector = [0.2, 0.8, -0.1, 0.5, 0.3]
print(vector)

print("\n--- Задание 2. Длина вектора ---")
print("Длина:", len(vector))

print("\n--- Задание 3. Первый и последний элементы ---")
print("Первый:", vector[0])
print("Последний:", vector[-1])

print("\n--- Задание 4. Два вектора одинаковой длины ---")
vector_a = [1.0, 0.0, 0.0]
vector_b = [0.9, 0.1, 0.0]
print("vector_a:", vector_a)
print("vector_b:", vector_b)
print("Длины равны:", len(vector_a) == len(vector_b))

print("\n--- Задание 5. cosine_similarity ---")
score_ab = cosine_similarity(vector_a, vector_b)
print("Сходство vector_a и vector_b:", round(score_ab, 4))

print("\n--- Задание 6. Три сравнения ---")
vector_c = [0.0, 0.0, 1.0]
score_ac = cosine_similarity(vector_a, vector_c)
print("a и b:", round(score_ab, 4))
print("a и c:", round(score_ac, 4))
print("Ближе vector_b:", score_ab > score_ac)

print("\n--- Задание 7. Вектор сам с собой ---")
score_aa = cosine_similarity(vector_a, vector_a)
print("Сходство vector_a с самим собой:", round(score_aa, 4))
