# Задание 6. Три столбца

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print(df[["Имя", "Группа", "Посещено"]])
