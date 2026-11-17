# Задание 12. Короткий документ
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

corpus_dir = Path("corpus")
short_path = corpus_dir / "short.txt"
short_path.write_text("Короткий текст.", encoding="utf-8")

for file_path in sorted(corpus_dir.glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    if len(text) < 50:
        print("Предупреждение: короткий документ", file_path.name)

short_path.unlink()
print("Временный файл удален")
