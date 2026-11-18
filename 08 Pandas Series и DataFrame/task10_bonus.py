# Задание 10. Бонус
import pandas as pd

data = {
    "Имя": ["Артем", "Анна", "Олег"],
    "Баллы": [85, 72, 91],
}

df = pd.DataFrame(data)
df["Баллы+5"] = df["Баллы"] + 5

print(df)
