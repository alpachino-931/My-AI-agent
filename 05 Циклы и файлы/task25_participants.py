# Задание 25. Список участников

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

participants = []

for number in range(1, 4):
    name = input("Введите имя участника " + str(number) + ": ")
    participants.append(name)

with open("participants.txt", "w", encoding="utf-8") as file:
    for participant in participants:
        file.write(participant + "\n")

print("Файл participants.txt создан")
