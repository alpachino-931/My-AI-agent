# Задание 23. Переименуйте столбец

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

df = df.rename(columns={"Баллы": "Тестовый балл"})

print(df)
