# Задание 25. Ошибка в вызове join
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

lines = ["Python", "pandas", "Git"]

clean_text = "\n".join(lines)

print(clean_text)
