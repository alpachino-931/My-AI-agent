# Звездочка 3. Сводка корпуса в CSV
import csv
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

rows = []
for file_path in sorted(Path("corpus").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    rows.append({
        "source": file_path.name,
        "category": categories.get(file_path.name, "без категории"),
        "chars": len(text)
    })

with open("corpus_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["source", "category", "chars"])
    writer.writeheader()
    writer.writerows(rows)

print("Файл corpus_summary.csv создан")
for row in rows:
    print(row["source"], "—", row["category"], "—", row["chars"])
