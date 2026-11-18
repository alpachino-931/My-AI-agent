# Задание 27. Анализ результатов теста

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("tests.csv")

result = df.groupby("Группа")[["Тест1", "Тест2"]].agg(["mean", "min", "max"])
print(result)

result.to_csv("tests_summary.csv", encoding="utf-8")

means = df.groupby("Группа")[["Тест1", "Тест2"]].mean().reset_index()
plt.plot(means["Группа"], means["Тест1"], marker="o", label="Тест1")
plt.plot(means["Группа"], means["Тест2"], marker="o", label="Тест2")
plt.title("Средние результаты тестов по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("tests_mean.png")
plt.show()

print("Файлы tests_summary.csv и tests_mean.png созданы")
