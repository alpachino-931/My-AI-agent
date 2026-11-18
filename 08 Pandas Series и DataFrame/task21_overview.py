# Задание 21. Быстрый обзор
import pandas as pd

data = {
    "Имя": ["Артем", "Анна", "Олег", "Мария"],
    "Баллы": [85, 72, 91, 64],
}

df = pd.DataFrame(data)

print(df.head())
print(df.tail())
df.info()
print(df.describe())

print("head и tail показывают несколько строк, info дает типы и размер, describe считает статистику.")
