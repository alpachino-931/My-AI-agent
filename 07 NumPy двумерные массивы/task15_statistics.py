# Задание 15. Общая статистика
import numpy as np

data = np.array([
    [4, 8, 15],
    [16, 23, 42],
    [1, 2, 3],
])

print("Сумма:", np.sum(data))
print("Среднее:", np.mean(data))
print("Минимум:", np.min(data))
print("Максимум:", np.max(data))
