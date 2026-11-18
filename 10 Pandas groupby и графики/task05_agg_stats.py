# Задание 5. Несколько показателей через agg()

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

stats = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max", "count"])

print(stats)
