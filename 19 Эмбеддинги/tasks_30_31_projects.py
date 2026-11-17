"""День 19, задания 30–31: мини-проекты по семантическому поиску."""

from embeddings import load_chunks, load_embedder, search

embedder = load_embedder()

print("--- Задание 30. Поиск по трём темам ---")
chunks = [
    {"source": "python.txt", "chunk_id": 0, "text": "Списки в Python создаются через квадратные скобки."},
    {"source": "python.txt", "chunk_id": 1, "text": "Функция print() выводит текст на экран."},
    {"source": "git.txt", "chunk_id": 0, "text": "git commit сохраняет изменения в истории."},
    {"source": "git.txt", "chunk_id": 1, "text": "git branch создаёт отдельную ветку."},
    {"source": "pandas.txt", "chunk_id": 0, "text": "DataFrame хранит табличные данные."},
    {"source": "pandas.txt", "chunk_id": 1, "text": "Pandas читает CSV через read_csv()."},
]
texts = [chunk["text"] for chunk in chunks]
chunk_embeddings = embedder.encode(texts)

questions = [
    "Как создать список?",
    "Как сохранить изменения в Git?",
    "Как прочитать CSV?",
]
for question in questions:
    best = search(embedder, chunks, chunk_embeddings, question)[0]
    print("\nВопрос:", question)
    print("Лучший чанк:", best["text"])
    print("source:", best["source"], "chunk_id:", best["chunk_id"])
    print("score:", round(best["score"], 4))

print("\n--- Задание 31. Поиск по корпусу Дня 18 ---")
corpus = load_chunks()
corpus_embeddings = embedder.encode([chunk["text"] for chunk in corpus])
print("Чанков в корпусе:", len(corpus))

questions = [
    "Почему возникает NameError?",
    "Как объявить функцию через def?",
    "Как открыть файл с помощью open()?",
    "Что делает list.append()?",
    "Как создать список в Python?",
]
for question in questions:
    best = search(embedder, corpus, corpus_embeddings, question)[0]
    print("\nВопрос:", question)
    print("source:", best["source"])
    print("chunk_id:", best["chunk_id"])
    print("score:", round(best["score"], 4))
    print("text:", best["text"][:100].replace("\n", " "))
