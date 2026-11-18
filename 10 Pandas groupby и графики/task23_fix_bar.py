# Задание 23. Исправленный bar: аргументы в круглых скобках

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")
result = df.groupby("Группа")["Баллы"].mean().reset_index()

plt.bar(result["Группа"], result["Баллы"])
plt.title("Средний балл по группам")
plt.show()
