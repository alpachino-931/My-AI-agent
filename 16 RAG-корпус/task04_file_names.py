# Задание 6. Имена файлов
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

corpus_dir = Path("corpus")
files = list(corpus_dir.glob("*.txt"))

for file_path in files:
    print(file_path.name)
