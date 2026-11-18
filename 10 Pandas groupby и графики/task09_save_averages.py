# Задание 9. Сохраните средние баллы

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Баллы"].mean().reset_index()
result.to_csv("average_by_group.csv", index=False, encoding="utf-8")

print(result)
print("Файл average_by_group.csv создан")
