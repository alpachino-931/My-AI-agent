# Задание 8. Чтение всех документов
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

files = list(Path("corpus").glob("*.txt"))
documents = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    documents.append(text)

print("Прочитано документов:", len(documents))
