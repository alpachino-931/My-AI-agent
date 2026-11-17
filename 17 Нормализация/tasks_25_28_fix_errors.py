"""День 17, задания 25–28: исправление ошибок в коде."""

from pathlib import Path

print("--- Задание 25. Ошибка split / join ---")
text = "Python    язык"
words = text.split(" ")
clean = " ".join(words)
print(clean)

print("\n--- Задание 26. Ошибка replace ---")
text = "Python\tGit"
print(repr(text.replace("\t", " ")))

print("\n--- Задание 27. Ошибка функции ---")


def clean_line(line):
    line = " ".join(line.split())
    return line


print(clean_line("  Python   язык  "))

print("\n--- Задание 28. Ошибка Path ---")
Path("normalized").mkdir(exist_ok=True)
print("mkdir(exist_ok=True) выполнен")
