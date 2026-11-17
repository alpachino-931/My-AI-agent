# Звездочка 1. Категория документа
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

categories = {
    "python_basics.txt": "основы",
    "python_lists.txt": "коллекции",
    "python_files.txt": "файлы",
    "python_functions.txt": "функции",
    "python_errors.txt": "ошибки",
    "python_strings.txt": "строки"
}

documents = []

for file_path in sorted(Path("corpus").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    document = {
        "source": file_path.name,
        "category": categories.get(file_path.name, "без категории"),
        "text": text
    }
    documents.append(document)

for document in documents:
    print(document["source"], "—", document["category"])
