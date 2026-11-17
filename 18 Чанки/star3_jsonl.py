"""День 18, звёздочка 3: сохранение всех чанков в JSONL.

Каждая строка файла chunks.jsonl — отдельный JSON-объект
с полями source, chunk_id, length и text.
"""

import json
from pathlib import Path

from chunking import split_with_overlap

CHUNK_SIZE = 300
OVERLAP = 50
MINIMUM_LENGTH = 30
JSONL_FILE = Path("chunks.jsonl")


def main() -> None:
    files = sorted(Path("normalized").glob("*.txt"))
    written = 0

    with open(JSONL_FILE, "w", encoding="utf-8") as output:
        for file_path in files:
            text = file_path.read_text(encoding="utf-8")
            chunks = split_with_overlap(text, CHUNK_SIZE, OVERLAP, MINIMUM_LENGTH)
            for chunk_id, chunk in enumerate(chunks):
                record = {
                    "source": file_path.name,
                    "chunk_id": chunk_id,
                    "length": len(chunk),
                    "text": chunk,
                }
                output.write(json.dumps(record, ensure_ascii=False) + "\n")
                written += 1

    print(f"Документов: {len(files)}")
    print(f"Записей в {JSONL_FILE.name}: {written}")

    print("\nПервые две строки файла:")
    with open(JSONL_FILE, encoding="utf-8") as source:
        for index, line in enumerate(source):
            if index >= 2:
                break
            print(line.rstrip())

    # Проверяем, что файл читается обратно и все записи корректны.
    restored = []
    with open(JSONL_FILE, encoding="utf-8") as source:
        for line in source:
            restored.append(json.loads(line))

    required = {"source", "chunk_id", "length", "text"}
    valid = all(required <= set(record) for record in restored)
    lengths_match = all(record["length"] == len(record["text"]) for record in restored)
    print(f"\nПрочитано записей: {len(restored)}")
    print(f"Все поля на месте: {valid}")
    print(f"Поле length совпадает с длиной text: {lengths_match}")


if __name__ == "__main__":
    main()
