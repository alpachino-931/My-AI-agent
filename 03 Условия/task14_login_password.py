# Задание 14. Проверка логина и пароля
login = "student"
password = "python123"

user_login = input("Введите логин: ")
user_password = input("Введите пароль: ")

if user_login == login and user_password == password:
    print("Доступ разрешен")
else:
    print("Неверный логин или пароль")
