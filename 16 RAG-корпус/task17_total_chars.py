# Задание 19. Общий объем корпуса
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

total_chars = 0

for file_path in sorted(Path("corpus").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    total_chars = total_chars + len(text)

print("Всего символов:", total_chars)
