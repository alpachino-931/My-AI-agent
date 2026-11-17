"""День 18, задания 30–31: мини-проекты по чанкингу."""

import csv
from pathlib import Path

from chunking import split_with_overlap

print("--- Задание 30. Один документ, два размера ---")
file_path = Path("normalized/python_errors.txt")
text = file_path.read_text(encoding="utf-8")

small = split_with_overlap(text, 200, 40)
large = split_with_overlap(text, 400, 80)
print("Документ:", file_path.name, "символов:", len(text))
print("200/40 → чанков:", len(small), "длины:", [len(chunk) for chunk in small])
print("400/80 → чанков:", len(large), "длины:", [len(chunk) for chunk in large])

print("\n--- Задание 31. Чанкинг всего корпуса Дня 17 ---")
chunks_dir = Path("chunks")
chunks_dir.mkdir(exist_ok=True)
all_chunks = []

for source_path in sorted(Path("normalized").glob("*.txt")):
    source_text = source_path.read_text(encoding="utf-8")
    for chunk_id, chunk in enumerate(split_with_overlap(source_text, 300, 50)):
        all_chunks.append({
            "source": source_path.name,
            "chunk_id": chunk_id,
            "length": len(chunk),
            "text": chunk,
        })
        filename = f"{source_path.stem}_chunk_{chunk_id}.txt"
        (chunks_dir / filename).write_text(chunk, encoding="utf-8")

with open("chunks_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])
    for chunk in all_chunks:
        writer.writerow([chunk["source"], chunk["chunk_id"], chunk["length"]])

print("Всего чанков:", len(all_chunks))
print("CSV и папка chunks обновлены")
