# Задание 5. Количество найденных файлов
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

corpus_dir = Path("corpus")
files = list(corpus_dir.glob("*.txt"))

print("Найдено файлов:", len(files))
