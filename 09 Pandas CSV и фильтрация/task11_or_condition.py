# Задание 11. Условие ИЛИ

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df[(df["Баллы"] >= 90) | (df["Посещено"] == 20)]

print(result)
