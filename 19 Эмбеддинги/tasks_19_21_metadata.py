"""День 19, задания 19–21: метаданные и embedding в словаре."""

from embeddings import load_embedder

embedder = load_embedder()

print("--- Задание 19. Словари чанков ---")
chunks = [
    {
        "source": "python.txt",
        "chunk_id": 0,
        "text": "Списки Python создаются с помощью квадратных скобок.",
    },
    {
        "source": "git.txt",
        "chunk_id": 0,
        "text": "Git commit сохраняет изменения в истории.",
    },
    {
        "source": "pandas.txt",
        "chunk_id": 0,
        "text": "DataFrame — основная таблица Pandas.",
    },
]
for chunk in chunks:
    print(chunk)

print("\n--- Задание 20. Список texts через обычный цикл ---")
texts = []
for chunk in chunks:
    texts.append(chunk["text"])
print("texts:", texts)
print("Количество текстов:", len(texts))

print("\n--- Задание 21. Embedding в каждом словаре ---")
chunk_embeddings = embedder.encode(texts)
for index in range(len(chunks)):
    chunks[index]["embedding"] = chunk_embeddings[index].tolist()

print("Поля первого чанка:", list(chunks[0].keys()))
print("Длина embedding:", len(chunks[0]["embedding"]))
nonzero = [value for value in chunks[0]["embedding"] if value != 0]
print("Ненулевых значений:", len(nonzero), "из", len(chunks[0]["embedding"]))
print("Первые 5 ненулевых чисел:", [round(value, 4) for value in nonzero[:5]])
