# Задание 26. Исправленная загрузка: read_csv вызывается через скобки

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print(df)
