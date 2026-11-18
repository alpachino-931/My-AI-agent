# День 3. Условия, сравнения и принятие решений
# Повторение типа bool
is_student = True
print(is_student)
print(type(is_student))

# Сравнения возвращают True или False
print(5 > 3)
print(5 < 3)

# = это присваивание, == это сравнение
age = 18
print(age == 18)

# Простое условие if + else
age = int(input("Введите возраст: "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

# Несколько вариантов: if / elif / else
number = int(input("Введите число: "))
if number > 0:
    print("Положительное число")
elif number < 0:
    print("Отрицательное число")
else:
    print("Это ноль")

# Логические операторы and, or, not
has_ticket = input("Есть билет? да/нет: ")
if age >= 18 and has_ticket == "да":
    print("Условия выполнены")
else:
    print("Условия не выполнены")

is_blocked = False
if not is_blocked:
    print("Доступ разрешен")
