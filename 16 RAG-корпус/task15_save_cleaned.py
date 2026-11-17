# Задание 17. Сохранение очищенных копий
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def clean_text(text):
    lines = text.splitlines()
    clean_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            clean_lines.append(line)
    return "\n".join(clean_lines)

corpus_dir = Path("corpus")
cleaned_dir = Path("cleaned")
cleaned_dir.mkdir(exist_ok=True)

for file_path in sorted(corpus_dir.glob("*.txt")):
    text = clean_text(file_path.read_text(encoding="utf-8"))
    if text == "":
        continue
    output_path = cleaned_dir / file_path.name
    output_path.write_text(text, encoding="utf-8")
    print("Сохранено:", output_path.name)
