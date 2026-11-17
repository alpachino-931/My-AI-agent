# Задание 21. Самый короткий документ
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

documents = []

for file_path in sorted(Path("corpus").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    if text.strip() != "":
        documents.append({"source": file_path.name, "text": text})

shortest = documents[0]
for document in documents:
    if len(document["text"]) < len(shortest["text"]):
        shortest = document

print("Самый короткий документ:", shortest["source"])
print("Символов:", len(shortest["text"]))
