# Задание 16. Процент посещаемости

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")
df["Процент посещаемости"] = (df["Посещено"] / 20 * 100).round(1)

print(df)
