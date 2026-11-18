# Задание 17. Бонусные баллы

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")
df["Баллы+5"] = df["Баллы"] + 5

print(df)
