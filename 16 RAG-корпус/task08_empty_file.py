# Задание 10. Пустой документ
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

corpus_dir = Path("corpus")
empty_path = corpus_dir / "empty.txt"
empty_path.write_text("", encoding="utf-8")

for file_path in sorted(corpus_dir.glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    if text.strip() == "":
        print("Пустой документ:", file_path.name)

empty_path.unlink()
print("Временный файл удален")
