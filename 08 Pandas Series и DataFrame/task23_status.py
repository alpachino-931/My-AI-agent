# Задание 23. Статус
import pandas as pd

data = {
    "Имя": ["Артем", "Анна", "Олег", "Мария"],
    "Баллы": [85, 72, 91, 64],
}

df = pd.DataFrame(data)
df["Статус"] = "учится"

print(df)
