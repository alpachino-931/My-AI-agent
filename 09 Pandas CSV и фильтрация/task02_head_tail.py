# Задание 2. Первые и последние строки

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print(df.head(3))
print(df.tail(2))
