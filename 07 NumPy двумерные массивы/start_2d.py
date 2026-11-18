# День 7. NumPy: двумерные массивы
import numpy as np

# Повторение одномерного массива
numbers = np.array([10, 20, 30, 40])
print(numbers)
print(numbers.shape)
print(numbers.ndim)

# Первый двумерный массив
data = np.array([
    [10, 20, 30],
    [40, 50, 60],
])
print(data)

# Характеристики массива
print("ndim:", data.ndim)
print("shape:", data.shape)
print("size:", data.size)

# Два индекса: строка и столбец
print(data[0, 0])
print(data[1, 2])

# Строка и столбец целиком
print(data[0])
print(data[:, 1])

# Изменение элемента и строки
data[0, 1] = 999
print(data)

data[1] = [1, 2, 3]
print(data)

# Двумерные срезы
table = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])
print(table[0:2])
print(table[0:2, 1:3])

# Арифметика со всей таблицей
small = np.array([[1, 2], [3, 4]])
print(small + 10)
print(small * 2)

# Статистика по всей таблице
stats = np.array([[10, 20], [30, 40]])
print(np.sum(stats))
print(np.mean(stats))
print(np.min(stats))
print(np.max(stats))

# axis=0 — по столбцам, axis=1 — по строкам
print(np.sum(stats, axis=0))
print(np.sum(stats, axis=1))
print(np.mean(stats, axis=0))
print(np.mean(stats, axis=1))

# arange() + reshape()
numbers = np.arange(1, 13)
print(numbers)
print(numbers.reshape(3, 4))

# Нули и единицы
print(np.zeros((2, 3)))
print(np.ones((3, 2)))

# Сравнение и фильтрация
scores = np.array([[45, 67, 82], [91, 53, 74]])
print(scores >= 60)
print(scores[scores >= 60])
