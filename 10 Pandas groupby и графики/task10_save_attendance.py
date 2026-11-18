# Задание 10. Средняя посещаемость по группам

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

result = df.groupby("Группа")["Посещено"].mean().reset_index()
result.to_csv("average_attendance.csv", index=False, encoding="utf-8")

print(result)
print("Файл average_attendance.csv создан")
