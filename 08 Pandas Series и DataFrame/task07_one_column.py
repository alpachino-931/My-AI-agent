# Задание 7. Один столбец
import pandas as pd

data = {
    "Имя": ["Артем", "Анна", "Олег"],
    "Баллы": [85, 72, 91],
}

df = pd.DataFrame(data)

print(df["Баллы"])
