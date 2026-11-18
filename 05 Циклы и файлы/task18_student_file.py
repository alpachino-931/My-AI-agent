# Задание 18. Анкета в файл

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
group = input("Введите группу: ")
speciality = input("Введите специальность: ")

with open("student.txt", "w", encoding="utf-8") as file:
    file.write("Имя: " + name + "\n")
    file.write("Фамилия: " + surname + "\n")
    file.write("Группа: " + group + "\n")
    file.write("Специальность: " + speciality + "\n")

print("Данные сохранены в student.txt")
