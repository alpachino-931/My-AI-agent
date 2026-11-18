# Задание 29. Исправленное сохранение: между аргументами нужна запятая

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

df.to_csv("result.csv", index=False, encoding="utf-8")

print("Файл result.csv создан")
