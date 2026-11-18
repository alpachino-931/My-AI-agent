# Задание 21. Исправленный groupby: метод вызывается через скобки

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Баллы"].mean().reset_index()

print(result)
