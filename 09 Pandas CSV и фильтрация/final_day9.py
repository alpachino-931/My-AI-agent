# Задание 32. Очистка и анализ учебных данных

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students_full.csv")

print("=" * 40)
print("Первые 5 строк:")
print(df.head(5))

print("=" * 40)
print("shape:", df.shape)
print("columns:", list(df.columns))
print("dtypes:")
print(df.dtypes)
df.info()

print("=" * 40)
print("Пропуски по столбцам:")
print(df.isna().sum())

print("=" * 40)
average_score = df["Баллы"].mean().round(1)
average_visits = df["Посещено"].median()
df["Баллы"] = df["Баллы"].fillna(average_score)
df["Посещено"] = df["Посещено"].fillna(average_visits)
df["Посещено"] = df["Посещено"].astype(int)
print("Баллы заполнены средним:", average_score)
print("Посещения заполнены медианой:", average_visits)
print(df)

print("=" * 40)
df["Пропущено"] = 20 - df["Посещено"]
df["Процент посещаемости"] = (df["Посещено"] / 20 * 100).round(1)
print(df)

print("=" * 40)
print("Баллы 80 и выше:")
high_scores = df[df["Баллы"] >= 80]
print(high_scores)

print("Группа 1ИИ-1:")
group_one = df[df["Группа"] == "1ИИ-1"]
print(group_one)

print("=" * 40)
result = df[(df["Баллы"] >= 70) & (df["Посещено"] >= 16)]
result = result.sort_values("Баллы", ascending=False)
result = result.reset_index(drop=True)
print("Итоговый фильтр:")
print(result)

print("=" * 40)
print("Средний балл:", df["Баллы"].mean())
print("Минимальный балл:", df["Баллы"].min())
print("Максимальный балл:", df["Баллы"].max())

result.to_csv("final_result_day9.csv", index=False, encoding="utf-8")
df.to_csv("cleaned_students_day9.csv", index=False, encoding="utf-8")
print("Файлы final_result_day9.csv и cleaned_students_day9.csv созданы")
