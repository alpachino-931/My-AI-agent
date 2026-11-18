# День 9. Pandas: CSV, фильтрация, сортировка и очистка

import os
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("students.csv")
print(df)

print("=" * 40)
print(df.head(3))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()

print("=" * 40)
print(df["Баллы"])
print(df[["Имя", "Баллы"]])

print("=" * 40)
print(df[df["Баллы"] >= 80])
print(df[df["Группа"] == "1ИИ-1"])
print(df[(df["Баллы"] >= 70) & (df["Посещено"] >= 16)])
print(df[(df["Баллы"] >= 90) | (df["Посещено"] == 20)])

print("=" * 40)
print(df.sort_values("Баллы"))
print(df.sort_values("Баллы", ascending=False))
print(df.sort_values(["Группа", "Баллы"], ascending=[True, False]))

print("=" * 40)
df["Пропущено"] = 20 - df["Посещено"]
df["Процент посещаемости"] = (df["Посещено"] / 20 * 100).round(1)
print(df)

print("=" * 40)
df = df.rename(columns={"Баллы": "Тестовый балл"})
print(df)

print("=" * 40)
missing_df = pd.read_csv("students_missing.csv")
print(missing_df)
print(missing_df.isna())
print(missing_df.isna().sum())
print(missing_df[missing_df["Баллы"].notna()])

average = missing_df["Баллы"].mean()
missing_df["Баллы"] = missing_df["Баллы"].fillna(average)
print(missing_df)

clean_df = missing_df.dropna()
clean_df = clean_df.reset_index(drop=True)
print(clean_df)

print("=" * 40)
result = df[(df["Тестовый балл"] >= 70) & (df["Посещено"] >= 16)]
result = result.sort_values("Тестовый балл", ascending=False)
print(result)
result.to_csv("result.csv", index=False, encoding="utf-8")
print("Файл result.csv создан")
