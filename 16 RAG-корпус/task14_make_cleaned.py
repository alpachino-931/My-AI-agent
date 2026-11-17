# Задание 16. Папка cleaned
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

cleaned_dir = Path("cleaned")
cleaned_dir.mkdir(exist_ok=True)

print("Папка cleaned существует:", cleaned_dir.exists())
