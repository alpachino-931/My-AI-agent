# Задание 5. Замена элемента
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])

data[1, 1] = 999

print(data)
