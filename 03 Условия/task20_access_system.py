# Задание 20. Мини-система доступа
age = int(input("Введите возраст: "))
pass_exists = input("Есть пропуск? да/нет: ")
escort = input("Есть сопровождение? да/нет: ")

if (age >= 18 and pass_exists == "да") or escort == "да":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
