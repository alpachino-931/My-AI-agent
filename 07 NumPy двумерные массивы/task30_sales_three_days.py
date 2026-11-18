# Задание 30. Продажи за три дня
import numpy as np

sales = np.array([
    [120, 90, 150, 60],
    [80, 100, 70, 110],
    [95, 130, 85, 75],
])

print("Общая сумма:", np.sum(sales))
print("Суммы по дням:", np.sum(sales, axis=1))
print("Суммы по товарам:", np.sum(sales, axis=0))
print("Общее среднее:", np.mean(sales))
