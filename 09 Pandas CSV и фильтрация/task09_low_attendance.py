# Задание 9. Низкая посещаемость

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print(df[df["Посещено"] < 16])
