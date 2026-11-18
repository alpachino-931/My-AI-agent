# Задание 13. Заголовок и подписи осей

import matplotlib.pyplot as plt

categories = ["А", "Б", "В"]
values = [12, 25, 18]

plt.bar(categories, values)
plt.title("Значения по категориям")
plt.xlabel("Категория")
plt.ylabel("Значение")
plt.show()
