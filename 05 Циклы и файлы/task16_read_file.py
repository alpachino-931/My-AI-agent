# Задание 16. Прочитай файл

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("hello.txt", "r", encoding="utf-8") as file:
    text = file.read()

print(text)
