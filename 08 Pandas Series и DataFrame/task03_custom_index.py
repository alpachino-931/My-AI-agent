# Задание 3. Свои индексы
import pandas as pd

temperatures = pd.Series(
    [21.5, 22.8, 20.4],
    index=["Пн", "Вт", "Ср"],
)

print(temperatures["Вт"])
