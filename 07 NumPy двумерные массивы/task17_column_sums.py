# Задание 17. Суммы столбцов
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])

print(np.sum(data, axis=0))
