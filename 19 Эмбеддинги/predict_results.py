"""День 19, уровень 9: предсказание результата."""

print("--- Предсказание 1 ---")
vector = [0.1, 0.2, 0.3]
print(len(vector))
print("Ожидалось: 3")

print("\n--- Предсказание 2 ---")
scores = [0.2, 0.8, 0.4]
best = max(scores)
print(scores.index(best))
print("Ожидалось: 1")

print("\n--- Предсказание 3 ---")
chunks = [{"source": "a.txt"}, {"source": "b.txt"}]
print(chunks[1]["source"])
print("Ожидалось: b.txt")
