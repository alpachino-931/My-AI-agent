# Задание 29. Подготовка корпуса для будущей RAG-системы
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

files = sorted(corpus_dir.glob("*.txt"))
documents = []
total_chars = 0

print("Документов в корпусе:", len(files))

for file_path in files:
    text = file_path.read_text(encoding="utf-8")

    if text.strip() == "":
        print("Пропущен пустой файл:", file_path.name)
        continue

    if len(text) < 50:
        print("Предупреждение: короткий документ", file_path.name)

    text = clean_text(text)
    documents.append({"source": file_path.name, "text": text})
    total_chars = total_chars + len(text)

    output_path = cleaned_dir / file_path.name
    output_path.write_text(text, encoding="utf-8")

print()
print("Документ                 Символов")
print("-" * 34)
for document in documents:
    print(f"{document['source']:<24}{len(document['text']):>8}")

print()
print("Всего символов:", total_chars)
print("Очищенные копии сохранены в папку cleaned")
