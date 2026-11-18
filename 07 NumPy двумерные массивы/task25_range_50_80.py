# Задание 25. Диапазон от 50 до 80
import numpy as np

data = np.array([
    [45, 67, 82],
    [91, 53, 74],
])

result = data[(data >= 50) & (data <= 80)]

print(result)
