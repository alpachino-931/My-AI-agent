# Задание 11. Длина каждого документа
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for file_path in sorted(Path("corpus").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    print(file_path.name, "—", len(text), "символов")
