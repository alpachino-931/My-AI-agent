# Задание 21. Заполнение средним

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

missing_df = pd.read_csv("students_missing.csv")

average = missing_df["Баллы"].mean()
missing_df["Баллы"] = missing_df["Баллы"].fillna(average)

print(missing_df)
