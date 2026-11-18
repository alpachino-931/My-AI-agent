# Задание 27. Мини-журнал учебной группы

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

names = ["Орлов", "Петрова", "Сидоров", "Козлова", "Морозов"]
scores = [78, 55, 91, 60, 44]

passed = 0
failed = 0

with open("group_report.txt", "w", encoding="utf-8") as file:
    for i in range(len(names)):
        if scores[i] >= 60:
            result = "зачет"
            passed = passed + 1
        else:
            result = "незачет"
            failed = failed + 1

        file.write(names[i] + " — " + str(scores[i]) + " — " + result + "\n")

    file.write("Зачет: " + str(passed) + "\n")
    file.write("Незачет: " + str(failed) + "\n")

with open("group_report.txt", "r", encoding="utf-8") as file:
    print("=== ЖУРНАЛ ГРУППЫ ===")
    print(file.read())
