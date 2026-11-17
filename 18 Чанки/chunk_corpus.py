"""День 18, раздел 43: чанкинг всего нормализованного корпуса.

Читает TXT-файлы из normalized/, режет их на чанки 300/50,
сохраняет чанки в chunks/ и сводку в chunks_summary.csv.
"""

import csv
import os
from pathlib import Path

from chunking import split_with_overlap

os.chdir(os.path.dirname(os.path.abspath(__file__)))

source_dir = Path("normalized")
chunks_dir = Path("chunks")
chunks_dir.mkdir(exist_ok=True)

for old_file in chunks_dir.glob("*.txt"):
    old_file.unlink()

files = sorted(source_dir.glob("*.txt"))
all_chunks = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    chunks = split_with_overlap(text, 300, 50)
    for chunk_id, chunk in enumerate(chunks):
        all_chunks.append({
            "source": file_path.name,
            "chunk_id": chunk_id,
            "text": chunk,
        })
        output_path = chunks_dir / f"{file_path.stem}_chunk_{chunk_id}.txt"
        output_path.write_text(chunk, encoding="utf-8")

with open("chunks_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])
    for chunk in all_chunks:
        writer.writerow([chunk["source"], chunk["chunk_id"], len(chunk["text"])])

print("Документов:", len(files))
print("Всего чанков:", len(all_chunks))
if all_chunks:
    average = sum(len(chunk["text"]) for chunk in all_chunks) / len(all_chunks)
    print("Средняя длина чанка:", round(average, 1))
