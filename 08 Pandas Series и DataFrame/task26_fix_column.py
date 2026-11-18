# Задание 26. Исправленный выбор столбца
import pandas as pd

data = {
    "Имя": ["Артем", "Анна"],
    "Баллы": [80, 90],
}

df = pd.DataFrame(data)

print(df["Баллы"])
print(df["Имя"])
