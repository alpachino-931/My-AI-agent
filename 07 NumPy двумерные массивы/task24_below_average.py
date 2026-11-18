# Задание 24. Ниже среднего
import numpy as np

scores = np.array([
    [45, 67, 82],
    [91, 53, 74],
])

average = np.mean(scores)

print("Общее среднее:", average)
print("Значения ниже среднего:", scores[scores < average])
