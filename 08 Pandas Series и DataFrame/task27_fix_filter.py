# Задание 27. Исправленный фильтр
import pandas as pd

data = {
    "Имя": ["Артем", "Анна"],
    "Баллы": [80, 90],
}

df = pd.DataFrame(data)

result = df[df["Баллы"] == 80]

print(result)
