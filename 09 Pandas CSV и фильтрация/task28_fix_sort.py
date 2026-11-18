# Задание 28. Исправленная сортировка: sort_values вызывается через скобки

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df.sort_values("Баллы", ascending=False)

print(result)
