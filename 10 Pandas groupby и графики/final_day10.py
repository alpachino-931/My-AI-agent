# Задание 28. Аналитический отчет по группам

import os
import pandas as pd
import matplotlib.pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")

print("=" * 40)
print("Первые 5 строк:")
print(df.head())
print("shape:", df.shape)
print("columns:", list(df.columns))
print("dtypes:")
print(df.dtypes)
df.info()

print("=" * 40)
print("Средний балл по группам:")
print(df.groupby("Группа")["Баллы"].mean().reset_index())
print("Минимальный балл:")
print(df.groupby("Группа")["Баллы"].min().reset_index())
print("Максимальный балл:")
print(df.groupby("Группа")["Баллы"].max().reset_index())
print("Количество студентов:")
print(df.groupby("Группа")["Имя"].count().reset_index())

print("=" * 40)
summary = df.groupby("Группа").agg(
    Средний_балл=("Баллы", "mean"),
    Минимум=("Баллы", "min"),
    Максимум=("Баллы", "max"),
    Количество=("Имя", "count"),
    Средняя_посещаемость=("Посещено", "mean"),
)
summary = summary.reset_index()
summary = summary.sort_values("Средний_балл", ascending=False).reset_index(drop=True)
print(summary)

summary.to_csv("group_summary.csv", index=False, encoding="utf-8")
print("Файл group_summary.csv создан")

print("=" * 40)
plt.bar(summary["Группа"], summary["Средний_балл"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid()
plt.tight_layout()
plt.savefig("group_summary.png")
plt.show()
print("Файл group_summary.png создан")

print("=" * 40)
plt.bar(summary["Группа"], summary["Средняя_посещаемость"])
plt.title("Средняя посещаемость по группам")
plt.xlabel("Группа")
plt.ylabel("Занятий")
plt.grid()
plt.tight_layout()
plt.savefig("group_attendance.png")
plt.show()

print("=" * 40)
df["Статус"] = "зачет"
print(df.groupby(["Группа", "Статус"])["Баллы"].mean().reset_index())

print("=" * 40)
print("Студенты с баллом выше среднего:")
average = df["Баллы"].mean()
print(df[df["Баллы"] > average])
