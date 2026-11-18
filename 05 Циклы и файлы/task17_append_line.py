# Задание 17. Добавь строку

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("hello.txt", "a", encoding="utf-8") as file:
    file.write("Добавленная строка\n")

with open("hello.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
