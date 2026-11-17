"""День 17, задания 9–14: дубли строк и служебные пометки."""

from text_normalization import SERVICE_LINES, clean_line, normalize_text

print("--- Задание 9. Точный дубль ---")
lines = ["Python — язык.", "Списки хранят элементы.", "Python — язык."]
unique_lines = []
for line in lines:
    if line not in unique_lines:
        unique_lines.append(line)
print(unique_lines)

print("\n--- Задание 10. Сохранение порядка ---")
print("Порядок сохранён:", unique_lines == ["Python — язык.", "Списки хранят элементы."])

print("\n--- Задание 11. Повтор с разным регистром ---")
print("Python".lower() == "python".lower())
print("Исходный текст не изменяем:", "Python и python — разные записи.")

print("\n--- Задание 12. Список служебных строк ---")
print(SERVICE_LINES)

print("\n--- Задание 13. Проверка без учёта регистра ---")
for line in ["Черновик", "ЧЕРНОВИК", "Служебная копия", "Полезная строка"]:
    normalized = clean_line(line).lower()
    print(f"{line!r}: удалить = {normalized in SERVICE_LINES}")

print("\n--- Задание 14. Похожая полезная строка остаётся ---")
text = "\n".join([
    "Черновик",
    "Полезная строка про черновик документа.",
    "Служебная копия",
    "Python — язык программирования.",
])
print(normalize_text(text, drop_service_lines=True))
