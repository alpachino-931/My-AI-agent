"""День 17, задания 1–8: пробелы, табуляции и строки документа."""

from text_normalization import clean_line, normalize_text

print("--- Задание 1. strip() ---")
text = "   Python   "
print("Было:", repr(text))
print("Стало:", repr(text.strip()))

print("\n--- Задание 2. Табуляция ---")
text = "Python\tGit\tPandas"
print("Было:", repr(text))
print("Стало:", repr(text.replace("\t", " ")))

print("\n--- Задание 3. Несколько пробелов ---")
text = "Python    язык    программирования"
print("Было:", repr(text))
print("Стало:", repr(" ".join(text.split())))

print("\n--- Задание 4. Функция clean_line() ---")
print(clean_line("  Python\t—   язык  "))

print("\n--- Задание 5. splitlines() ---")
multi = "Первая строка\nВторая строка\nТретья строка"
print(multi.splitlines())

print("\n--- Задание 6. Пустые строки ---")
lines = ["A", "", "  ", "B"]
clean_lines = []
for line in lines:
    line = clean_line(line)
    if line != "":
        clean_lines.append(line)
print("Было:", lines)
print("Стало:", clean_lines)

print("\n--- Задание 7. Сборка через \\n.join() ---")
result = "\n".join(clean_lines)
print(repr(result))

print("\n--- Задание 8. Сравнение до и после ---")
dirty = "  Python   —  язык.\t\n\n  Python   —  язык.\n  Списки   хранят  элементы.  "
print("Исходный текст:")
print(dirty)
print("Очищенный текст:")
print(normalize_text(dirty))
