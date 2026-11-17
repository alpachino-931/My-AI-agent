# Звездочка 2. Средняя длина документа
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lengths = []

for file_path in sorted(Path("corpus").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    lengths.append(len(text))

average = sum(lengths) / len(lengths)

print("Документов:", len(lengths))
print("Средняя длина:", round(average, 1), "символов")
