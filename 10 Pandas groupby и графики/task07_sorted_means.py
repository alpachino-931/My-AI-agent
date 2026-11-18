# Задание 7. Сортировка среднего балла

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Баллы"].mean().reset_index()
result = result.sort_values("Баллы", ascending=False).reset_index(drop=True)

print(result)
