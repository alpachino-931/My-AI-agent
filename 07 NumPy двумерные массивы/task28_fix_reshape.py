# Задание 28. Исправленная reshape(): 12 элементов -> 3 x 4

import numpy as np

numbers = np.arange(1, 13)
table = numbers.reshape(3, 4)

print(table)
