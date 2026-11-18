# Задание 10. Допуск к мероприятию
age = int(input("Введите возраст: "))
registration = input("Есть регистрация? да/нет: ")

if age >= 16 and registration == "да":
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
