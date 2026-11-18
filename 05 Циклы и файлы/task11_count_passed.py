# Задание 11. Количество зачетов

scores = [45, 78, 91, 53, 60, 39, 88, 75]
count = 0

for score in scores:
    if score >= 60:
        count = count + 1

print("Количество зачетов:", count)
