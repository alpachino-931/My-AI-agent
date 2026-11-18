# Задание 31. Температуры
import numpy as np

temps = np.array([
    [21.5, 22.0, 19.8, 23.1, 20.4],
    [18.9, 24.0, 21.2, 20.5, 19.6],
    [23.5, 22.8, 21.0, 18.4, 20.9],
])

average = np.mean(temps)

print("Среднее каждого дня:", np.mean(temps, axis=1))
print("Среднее каждого столбца:", np.mean(temps, axis=0))
print("Общее среднее:", average)
print("Значения выше общего среднего:", temps[temps > average])
