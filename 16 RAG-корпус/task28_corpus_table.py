# Задание 28. Таблица корпуса
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("Документ                 Символов")
print("-" * 34)

for file_path in sorted(Path("corpus").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    print(f"{file_path.name:<24}{len(text):>8}")
