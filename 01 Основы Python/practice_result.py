# Итоговое практическое задание. Рабочее окружение и colorama
from colorama import Fore, Style

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
group = input("Введите группу: ")
speciality = input("Введите специальность: ")
interest = input("Введите интересующую область IT: ")

print(Fore.CYAN + "========================================")
print(Fore.CYAN + "       РЕЗУЛЬТАТ ПРАКТИЧЕСКОЙ РАБОТЫ")
print(Fore.CYAN + "========================================")
print(Fore.GREEN + "Имя: " + name)
print(Fore.GREEN + "Фамилия: " + surname)
print(Fore.GREEN + "Группа: " + group)
print(Fore.GREEN + "Специальность: " + speciality)
print(Fore.GREEN + "Интерес: " + interest)
print(Fore.YELLOW + "Рабочее окружение подготовлено")
print(Style.RESET_ALL)
