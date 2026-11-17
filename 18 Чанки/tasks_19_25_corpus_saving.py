"""День 18, задания 19–25: чанкинг всего корпуса и сохранение."""

import csv
from pathlib import Path

from chunking import split_with_overlap

print("--- Задание 19. Все TXT ---")
files = sorted(Path("normalized").glob("*.txt"))
print("Документов:", len(files))

print("\n--- Задания 20–22. all_chunks, количество и средняя длина ---")
all_chunks = []
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    for chunk_id, chunk in enumerate(split_with_overlap(text, 300, 50)):
        all_chunks.append({
            "source": file_path.name,
            "chunk_id": chunk_id,
            "length": len(chunk),
            "text": chunk,
        })

print("Всего чанков:", len(all_chunks))
average = sum(chunk["length"] for chunk in all_chunks) / len(all_chunks) if all_chunks else 0
print("Средняя длина:", round(average, 1))

print("\n--- Задания 23–24. Папка chunks и имена файлов ---")
chunks_dir = Path("chunks")
chunks_dir.mkdir(exist_ok=True)
for chunk in all_chunks:
    filename = f"{Path(chunk['source']).stem}_chunk_{chunk['chunk_id']}.txt"
    (chunks_dir / filename).write_text(chunk["text"], encoding="utf-8")
print("Файлов в chunks:", len(list(chunks_dir.glob("*.txt"))))

print("\n--- Задание 25. CSV-сводка ---")
with open("chunks_summary.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["source", "chunk_id", "length"])
    for chunk in all_chunks:
        writer.writerow([chunk["source"], chunk["chunk_id"], chunk["length"]])
print("chunks_summary.csv создан")
