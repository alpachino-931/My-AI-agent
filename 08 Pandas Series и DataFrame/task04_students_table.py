# Задание 4. Таблица студентов
import pandas as pd

data = {
    "Имя": ["Артем", "Анна", "Олег"],
    "Баллы": [85, 72, 91],
}

df = pd.DataFrame(data)

print(df)
