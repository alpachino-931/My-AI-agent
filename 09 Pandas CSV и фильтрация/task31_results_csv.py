# Задание 31. Таблица результатов из CSV

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("results.csv")
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()

df["Процент посещаемости"] = (df["Посещено"] / 20 * 100).round(1)
print(df)

result = df[df["Баллы"] >= 70]
result = result.sort_values("Баллы", ascending=False)
print(result)

result.to_csv("results_filtered.csv", index=False, encoding="utf-8")
print("Файл results_filtered.csv создан")
