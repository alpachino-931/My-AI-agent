# Задание 9. Источник и текст
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

files = list(Path("corpus").glob("*.txt"))
documents = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    document = {
        "source": file_path.name,
        "text": text
    }
    documents.append(document)

print(documents[0]["source"])
print(documents[0]["text"].splitlines()[0])
