# Задание 29. Результаты двух групп
import numpy as np

scores = np.array([
    [78, 85, 60, 92, 70],
    [55, 68, 74, 81, 63],
])

print("Среднее по каждой группе:", np.mean(scores, axis=1))
print("Среднее по каждому заданию:", np.mean(scores, axis=0))
print("Минимум:", np.min(scores))
print("Максимум:", np.max(scores))
