"""День 18, задания 9–14: очистка чанков и метаданные."""

from chunking import split_with_overlap

text = "  Python — язык программирования.   Переменные хранят значения.  "

print("--- Задание 9. strip() ---")
chunk = text[0:30]
print(repr(chunk))
print(repr(chunk.strip()))

print("\n--- Задание 10. Пустой фрагмент ---")
parts = ["Python", "", "   ", "Списки"]
print([part for part in parts if part.strip() != ""])

print("\n--- Задание 11. minimum_length = 20 ---")
long_text = (
    "Python — язык программирования. Функции объявляются через def. "
    "Списки хранят элементы. Конец."
)
raw_chunks = [
    long_text[start:start + 40].strip()
    for start in range(0, len(long_text), 30)
]
print("Все фрагменты:", raw_chunks)
print("После порога 20:", split_with_overlap(long_text, 40, 10, minimum_length=20))

print("\n--- Задания 12–14. source, chunk_id, length ---")
chunks = split_with_overlap(long_text, 25, 5, minimum_length=10)
result = []
for chunk_id, chunk in enumerate(chunks):
    result.append({
        "source": "python_functions.txt",
        "chunk_id": chunk_id,
        "length": len(chunk),
        "text": chunk,
    })

for item in result:
    print(item)
