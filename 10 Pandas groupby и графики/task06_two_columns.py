# Задание 6. Два числовых столбца

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df.groupby("Группа")[["Баллы", "Посещено"]].mean()

print(result)
