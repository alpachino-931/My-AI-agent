# Задание 18. Маркеры на линии

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

plt.plot(df["Имя"], df["Баллы"], marker="o")
plt.title("Баллы студентов")
plt.xlabel("Студент")
plt.ylabel("Баллы")
plt.show()
