# День 5. Циклы и работа с текстовыми файлами

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Цикл for по списку
languages = ["Python", "Java", "C++"]
for language in languages:
    print(language)

# Цикл и условие
scores = [45, 78, 91, 53]
for score in scores:
    if score >= 60:
        print(score, "— зачет")
    else:
        print(score, "— незачет")

# range(): начало, конец (не включается), шаг
for number in range(1, 6):
    print(number)

for number in range(0, 11, 2):
    print(number)

# Накопление суммы
numbers = [10, 20, 30]
total = 0
for number in numbers:
    total = total + number
print("Сумма:", total)

# Цикл while
number = 1
while number <= 5:
    print(number)
    number = number + 1

# break и continue
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# Запись в файл
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")

# Добавление в конец файла
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("Новая строка\n")

# Чтение файла целиком
with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)

# Чтение построчно и strip()
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
