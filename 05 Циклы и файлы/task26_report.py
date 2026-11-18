# Задание 26. Отчет по списку

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

scores = [45, 78, 91, 53, 60, 39, 88]
passed = 0
failed = 0

for score in scores:
    if score >= 60:
        passed = passed + 1
    else:
        failed = failed + 1

with open("report.txt", "w", encoding="utf-8") as file:
    file.write("Зачет: " + str(passed) + "\n")
    file.write("Незачет: " + str(failed) + "\n")

with open("report.txt", "r", encoding="utf-8") as file:
    print(file.read())
