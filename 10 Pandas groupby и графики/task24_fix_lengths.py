# Задание 24. Исправленная длина данных: трем категориям нужны три значения

import matplotlib.pyplot as plt

groups = ["A", "B", "C"]
scores = [10, 20, 30]

plt.bar(groups, scores)
plt.title("Три категории и три значения")
plt.show()
