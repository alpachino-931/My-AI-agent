# Задание 6. Характеристики таблицы
import pandas as pd

data = {
    "Имя": ["Артем", "Анна", "Олег"],
    "Баллы": [85, 72, 91],
}

df = pd.DataFrame(data)

print(df.shape)
print(df.columns)
print(df.index)
