# Задание 13. Лишние пробелы
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = Path("corpus/python_files.txt").read_text(encoding="utf-8")
lines = text.splitlines()
clean_lines = []

for line in lines:
    clean_lines.append(line.strip())

with_spaces = 0
for line in lines:
    if line != line.strip():
        with_spaces = with_spaces + 1

print("Строк в файле:", len(lines))
print("Строк с лишними пробелами:", with_spaces)
print("Первая строка:", clean_lines[0])
print("Последняя строка:", clean_lines[-1])
