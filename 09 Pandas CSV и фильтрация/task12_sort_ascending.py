# Задание 12. Сортировка по баллам

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print(df.sort_values("Баллы"))
