# День 8. Pandas: Series, DataFrame и обработка таблиц
import pandas as pd

print("Pandas подключена")
print(pd.__version__)

# Series и индексы
scores = pd.Series([70, 80, 90, 65])
print(scores)
print(scores[0])
print(scores[2])

scores = pd.Series(
    [70, 80, 90],
    index=["Иванов", "Петров", "Сидорова"],
)
print(scores["Петров"])

# DataFrame из словаря
data = {
    "Имя": ["Артем", "Анна", "Олег"],
    "Баллы": [85, 72, 91],
}
df = pd.DataFrame(data)
print(df)

# Характеристики таблицы
print(df.shape)
print(df.columns)
print(df.index)

# Выбор столбцов
print(df["Баллы"])
print(df[["Имя", "Баллы"]])

# Новые столбцы
df["Группа"] = ["1ИИ-1", "1ИИ-1", "1ИИ-2"]
df["Курс"] = 1
df["Баллы"] = df["Баллы"] + 5
df["Баллы после бонуса"] = df["Баллы"] + 10
print(df)

# loc и iloc
print(df.loc[0])
print(df.iloc[1])
print(df.loc[0, "Имя"])
print(df.iloc[0:2])

# Фильтрация
print(df[df["Баллы"] >= 80])
print(df[df["Группа"] == "1ИИ-1"])
print(df[(df["Баллы"] >= 70) & (df["Баллы"] <= 90)])

# Статистика
print(df["Баллы"].sum())
print(df["Баллы"].mean())
print(df["Баллы"].min())
print(df["Баллы"].max())
print(df["Баллы"].count())

# Обзор таблицы
print(df.head())
print(df.head(2))
print(df.tail(2))
df.info()
print(df.dtypes)
print(df.describe())
