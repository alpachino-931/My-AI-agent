# Задание 15. Пропуски занятий

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")
df["Пропущено"] = 20 - df["Посещено"]

print(df)
