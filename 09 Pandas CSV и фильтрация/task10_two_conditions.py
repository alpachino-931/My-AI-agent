# Задание 10. Два условия

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df[(df["Баллы"] >= 75) & (df["Посещено"] >= 16)]

print(result)
