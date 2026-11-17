# Задание 22. Ошибка в шаблоне glob
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

corpus_dir = Path("corpus")
wrong = list(corpus_dir.glob("txt"))
right = list(corpus_dir.glob("*.txt"))

print("Шаблон txt нашел файлов:", len(wrong))
print("Шаблон *.txt нашел файлов:", len(right))
