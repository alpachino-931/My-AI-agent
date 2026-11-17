# Задание 18. Сравнение исходного и очищенного файла
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

source_text = Path("corpus/python_files.txt").read_text(encoding="utf-8")
lines = source_text.splitlines()
clean_lines = []

for line in lines:
    line = line.strip()
    if line != "":
        clean_lines.append(line)

cleaned_text = "\n".join(clean_lines)

print("Символов в исходнике:", len(source_text))
print("Символов после очистки:", len(cleaned_text))
print("Строк в исходнике:", len(lines))
print("Строк после очистки:", len(clean_lines))
