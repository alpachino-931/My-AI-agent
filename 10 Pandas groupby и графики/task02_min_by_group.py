# Задание 2. Минимальный балл по группам

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print(df.groupby("Группа")["Баллы"].min().reset_index())
