# Задание 14. Пустые строки
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = Path("corpus/python_files.txt").read_text(encoding="utf-8")
lines = text.splitlines()
clean_lines = []

for line in lines:
    line = line.strip()
    if line != "":
        clean_lines.append(line)

print("Строк до очистки:", len(lines))
print("Строк после очистки:", len(clean_lines))
print("\n".join(clean_lines))
