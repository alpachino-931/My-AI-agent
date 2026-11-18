from colorama import Fore, Style 

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
group = input("Введите группу: ")

print(Fore.GREEN + "=== КАРТОЧКА ===")
print(Fore.CYAN + "Имя: " + name)
print(Fore.CYAN + "Фамилия: " + surname)
print(Fore.CYAN + "Группа: " + group)
print(Style.RESET_ALL)