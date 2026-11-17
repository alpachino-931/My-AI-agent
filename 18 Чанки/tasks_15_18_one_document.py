"""День 18, задания 15–18: чанкинг одного документа.

Для документа python_errors.txt (374 символа) параметры 200/40 дают
ровно три чанка, поэтому на нём удобно показать перекрытие.
"""

from pathlib import Path

from chunking import split_with_overlap

print("--- Задание 15. Чтение одного файла ---")
file_path = Path("normalized/python_errors.txt")
text = file_path.read_text(encoding="utf-8")
print("Файл:", file_path.name, "символов:", len(text))

print("\n--- Задание 16. Разбиение 200 / 40 ---")
chunks = split_with_overlap(text, chunk_size=200, overlap=40)
print("Чанков:", len(chunks))

print("\n--- Задание 17. Номер и длина каждого чанка ---")
for chunk_id, chunk in enumerate(chunks):
    print(f"Чанк {chunk_id}: длина {len(chunk)}")

print("\n--- Задание 18. Три соседних чанка ---")
for chunk_id, chunk in enumerate(chunks[:3]):
    print(f"\nЧанк {chunk_id}:")
    print(chunk)
