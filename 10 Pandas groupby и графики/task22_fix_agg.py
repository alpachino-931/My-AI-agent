# Задание 22. Исправленный agg: список операций передается одним аргументом

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max"])

print(result)
