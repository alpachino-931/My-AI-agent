# Задание 26. Анализ товаров по категориям

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("products.csv")

result = df.groupby("Категория").agg(
    Средняя_цена=("Цена", "mean"),
    Всего_единиц=("Количество", "sum"),
)
result = result.reset_index()
print(result)

result.to_csv("products_summary.csv", index=False, encoding="utf-8")

plt.bar(result["Категория"], result["Средняя_цена"])
plt.title("Средняя цена по категориям")
plt.xlabel("Категория")
plt.ylabel("Средняя цена")
plt.grid()
plt.tight_layout()
plt.savefig("products_price.png")
plt.show()

print("Файлы products_summary.csv и products_price.png созданы")
