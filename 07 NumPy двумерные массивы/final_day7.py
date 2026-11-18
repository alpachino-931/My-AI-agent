# Задание 32. Анализ результатов учебных групп

import numpy as np

data = np.array([
    [78, 85, 60, 92, 70],
    [55, 68, 74, 81, 63],
    [90, 88, 95, 72, 84],
])

print("Исходная таблица:")
print(data)

print("shape:", data.shape)
print("ndim:", data.ndim)
print("size:", data.size)

overall_mean = np.mean(data)

print("Общее среднее:", overall_mean)
print("Среднее каждой группы:", np.mean(data, axis=1))
print("Среднее каждого задания:", np.mean(data, axis=0))
print("Минимум:", np.min(data))
print("Максимум:", np.max(data))
print("Значения 60 и выше:", data[data >= 60])
print("Значения ниже общего среднего:", data[data < overall_mean])
print("Первая строка:", data[0])
print("Последний столбец:", data[:, -1])
print("Фрагмент 2 x 2:")
print(data[0:2, 0:2])

data[1, 0] = 59
print("После изменения элемента data[1, 0]:")
print(data)

new_data = data + 5
print("Новая таблица после прибавления 5:")
print(new_data)
print("Новое общее среднее:", np.mean(new_data))
