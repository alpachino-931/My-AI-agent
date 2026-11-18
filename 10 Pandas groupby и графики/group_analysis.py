# День 10. Pandas: группировка и агрегация. Основы Matplotlib

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")
print(df.head())

print("=" * 40)
print(df.groupby("Группа")["Баллы"].mean().reset_index())
print(df.groupby("Группа")["Баллы"].sum().reset_index())
print(df.groupby("Группа")["Баллы"].min().reset_index())
print(df.groupby("Группа")["Баллы"].max().reset_index())
print(df.groupby("Группа")["Имя"].count().reset_index())

print("=" * 40)
stats = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max", "count"])
print(stats)

print("=" * 40)
result = df.groupby("Группа")[["Баллы", "Посещено"]].mean()
print(result)

print("=" * 40)
df["Статус"] = "зачет"
print(df.groupby(["Группа", "Статус"])["Баллы"].mean().reset_index())

print("=" * 40)
result = df.groupby("Группа")["Баллы"].mean().reset_index()
result = result.sort_values("Баллы", ascending=False).reset_index(drop=True)
print(result)
result.to_csv("group_result.csv", index=False, encoding="utf-8")

print("=" * 40)
plt.bar(result["Группа"], result["Баллы"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid()
plt.tight_layout()
plt.savefig("chart.png")
plt.show()

print("=" * 40)
plt.plot(df["Имя"], df["Баллы"], marker="o")
plt.title("Баллы студентов")
plt.xlabel("Студент")
plt.ylabel("Баллы")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.savefig("students_chart.png")
plt.show()

print("Файлы group_result.csv, chart.png и students_chart.png созданы")
