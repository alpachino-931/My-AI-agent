# Задание 28. Исправленные условия
import pandas as pd

data = {
    "Имя": ["Артем", "Анна", "Олег", "Мария"],
    "Баллы": [85, 72, 91, 64],
}

df = pd.DataFrame(data)

result = df[(df["Баллы"] >= 70) & (df["Баллы"] <= 90)]

print(result)
