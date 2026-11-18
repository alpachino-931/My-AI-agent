# Задание 6. Поиск технологии

technologies = ["Python", "Git", "SQL", "Docker", "Linux"]

answer = input("Введите технологию: ")

if answer in technologies:
    print("Технология есть в списке")
else:
    print("Такой технологии в списке нет")
