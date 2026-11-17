"""День 18, задание 32: подготовка чанков для будущего векторного поиска.

Программа:
1. находит все TXT-файлы в normalized/;
2. читает каждый документ;
3. делит текст на чанки (chunk_size=300, overlap=50);
4. проверяет корректность параметров;
5. удаляет пробелы по краям;
6. не сохраняет пустые и слишком короткие чанки;
7. хранит source, chunk_id и length;
8. создаёт папку chunks/ и сохраняет каждый чанк в TXT;
9. создаёт chunks_summary.csv;
10. выводит число документов, чанков и среднюю длину;
11. проверяет, что нет чанков длиннее chunk_size и короче minimum_length.
"""

import csv
import os
from pathlib import Path

from chunking import split_with_overlap

os.chdir(os.path.dirname(os.path.abspath(__file__)))

SOURCE_DIR = Path("normalized")
CHUNKS_DIR = Path("chunks")
CSV_FILE = Path("chunks_summary.csv")
CHUNK_SIZE = 300
OVERLAP = 50
MINIMUM_LENGTH = 30

CHUNKS_DIR.mkdir(exist_ok=True)
for old_file in CHUNKS_DIR.glob("*.txt"):
    old_file.unlink()

files = sorted(SOURCE_DIR.glob("*.txt"))
if not files:
    print("В папке normalized нет TXT-файлов.")
    raise SystemExit(1)

all_chunks = []

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    chunks = split_with_overlap(
        text,
        chunk_size=CHUNK_SIZE,
        overlap=OVERLAP,
        minimum_length=MINIMUM_LENGTH,
    )

    for chunk_id, chunk in enumerate(chunks):
        data = {
            "source": file_path.name,
            "chunk_id": chunk_id,
            "length": len(chunk),
            "text": chunk,
        }
        all_chunks.append(data)

        filename = f"{file_path.stem}_chunk_{chunk_id}.txt"
        (CHUNKS_DIR / filename).write_text(chunk, encoding="utf-8")

with open(CSV_FILE, "w", encoding="utf-8", newline="") as report:
    writer = csv.writer(report)
    writer.writerow(["source", "chunk_id", "length"])
    for chunk in all_chunks:
        writer.writerow([chunk["source"], chunk["chunk_id"], chunk["length"]])

total_length = sum(chunk["length"] for chunk in all_chunks)
average = total_length / len(all_chunks) if all_chunks else 0

print(f"Документов: {len(files)}")
print(f"Всего чанков: {len(all_chunks)}")
print(f"Средняя длина чанка: {round(average, 1)}")

empty_chunks = [chunk for chunk in all_chunks if chunk["text"] == ""]
too_long = [chunk for chunk in all_chunks if chunk["length"] > CHUNK_SIZE]
too_short = [chunk for chunk in all_chunks if chunk["length"] < MINIMUM_LENGTH]

print(f"Пустых чанков: {len(empty_chunks)}")
print(f"Чанков длиннее {CHUNK_SIZE}: {len(too_long)}")
print(f"Чанков короче {MINIMUM_LENGTH}: {len(too_short)}")
print(f"Метаданные и тексты сохранены в {CHUNKS_DIR.name}/ и {CSV_FILE.name}")
