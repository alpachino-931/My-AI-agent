# Задание 20. Самый длинный документ
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

documents = []

for file_path in sorted(Path("corpus").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    documents.append({"source": file_path.name, "text": text})

longest = documents[0]
for document in documents:
    if len(document["text"]) > len(longest["text"]):
        longest = document

print("Самый длинный документ:", longest["source"])
print("Символов:", len(longest["text"]))
