# Задание 20. Прочитай построчно

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("technologies.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
