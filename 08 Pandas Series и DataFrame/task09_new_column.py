# Задание 9. Новый столбец
import pandas as pd

data = {
    "Имя": ["Артем", "Анна", "Олег"],
    "Баллы": [85, 72, 91],
}

df = pd.DataFrame(data)
df["Курс"] = 1

print(df)
