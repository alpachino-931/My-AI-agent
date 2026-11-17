# Задание 27. Корпус по своей теме
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

corpus_dir = Path("corpus_git")
documents = []

for file_path in sorted(corpus_dir.glob("*.txt")):
    text = clean_text(file_path.read_text(encoding="utf-8"))
    if text == "":
        continue
    documents.append({"source": file_path.name, "text": text})

print("Тема: Git")
print("Документов:", len(documents))
for document in documents:
    print(document["source"], "—", len(document["text"]), "символов")
