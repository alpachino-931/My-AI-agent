# Задание 23. Исправленная программа: запятые, двоеточие, отступ

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Привет")

print("Файл data.txt создан")
