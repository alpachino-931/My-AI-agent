# Задание 15. Функция clean_text
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def clean_text(text):
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)
    return "\n".join(clean_lines)

text = Path("corpus/python_files.txt").read_text(encoding="utf-8")

print(clean_text(text))
