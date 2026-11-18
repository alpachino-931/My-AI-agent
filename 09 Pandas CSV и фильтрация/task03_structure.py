# Задание 3. Структура

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()
