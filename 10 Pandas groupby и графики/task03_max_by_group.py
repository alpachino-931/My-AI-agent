# Задание 3. Максимальный балл по группам

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print(df.groupby("Группа")["Баллы"].max().reset_index())
