# Задание 7. Чтение одного документа
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = Path("corpus/python_basics.txt").read_text(encoding="utf-8")

print(text)
