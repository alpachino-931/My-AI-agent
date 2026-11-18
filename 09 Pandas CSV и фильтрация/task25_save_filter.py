# Задание 25. Сохраните фильтр

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df[df["Баллы"] >= 80]
result.to_csv("high_scores.csv", index=False, encoding="utf-8")

print(result)
