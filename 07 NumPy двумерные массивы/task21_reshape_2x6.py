# Задание 21. 12 чисел -> 2 x 6
import numpy as np

numbers = np.arange(1, 13)
table = numbers.reshape(2, 6)

print(table)
