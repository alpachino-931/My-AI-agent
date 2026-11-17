"""День 18, звёздочка 2: нумерация документов через document_index.

Каждый исходный файл получает собственный номер, а каждый чанк хранит
source, document_index, chunk_id и length. Сводка пишется в CSV.
"""

import csv
from pathlib import Path

from chunking import split_with_overlap

CHUNK_SIZE = 300
OVERLAP = 50
MINIMUM_LENGTH = 30


def main() -> None:
    files = sorted(Path("normalized").glob("*.txt"))
    all_chunks = []

    for document_index, file_path in enumerate(files):
        text = file_path.read_text(encoding="utf-8")
        chunks = split_with_overlap(text, CHUNK_SIZE, OVERLAP, MINIMUM_LENGTH)
        for chunk_id, chunk in enumerate(chunks):
            all_chunks.append({
                "document_index": document_index,
                "source": file_path.name,
                "chunk_id": chunk_id,
                "length": len(chunk),
                "text": chunk,
            })

    print("document_index  source                          chunk_id  length")
    print("-" * 66)
    for chunk in all_chunks:
        print(
            f"{chunk['document_index']:>14}  {chunk['source']:<30}"
            f"{chunk['chunk_id']:>9}{chunk['length']:>8}"
        )

    with open("chunks_with_index.csv", "w", encoding="utf-8", newline="") as report:
        writer = csv.writer(report)
        writer.writerow(["document_index", "source", "chunk_id", "length"])
        for chunk in all_chunks:
            writer.writerow([
                chunk["document_index"],
                chunk["source"],
                chunk["chunk_id"],
                chunk["length"],
            ])

    print(f"\nДокументов: {len(files)}")
    print(f"Всего чанков: {len(all_chunks)}")
    print("Сводка сохранена в chunks_with_index.csv")


if __name__ == "__main__":
    main()
