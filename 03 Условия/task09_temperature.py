# Задание 9. Температура
temperature = float(input("Введите температуру: "))

if temperature > 25:
    print("Жарко")
elif temperature >= 15:
    print("Тепло")
elif temperature >= 0:
    print("Прохладно")
else:
    print("Холодно")
