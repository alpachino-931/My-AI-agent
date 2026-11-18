# Задание 20. Только заполненные баллы

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

missing_df = pd.read_csv("students_missing.csv")

print(missing_df[missing_df["Баллы"].notna()])
