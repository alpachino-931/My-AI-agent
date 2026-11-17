# Задание 1. Папка корпуса
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

corpus_dir = Path("corpus")
files = sorted(corpus_dir.glob("*.txt"))

print("Папка корпуса:", corpus_dir)
print("Файлов в корпусе:", len(files))
for file_path in files:
    lines = file_path.read_text(encoding="utf-8").splitlines()
    print(file_path.name, "|", len(lines), "строк")
