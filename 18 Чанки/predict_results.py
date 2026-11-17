"""День 18, уровень 9: предсказание результата."""

print("--- Предсказание 1 ---")
text = "ABCDEFGHIJ"
print(repr(text[0:4]))
print("Ожидалось: 'ABCD'")

print("\n--- Предсказание 2 ---")
chunk_size = 10
overlap = 3
step = chunk_size - overlap
print(step)
print("Ожидалось: 7")

print("\n--- Предсказание 3 ---")
chunks = ["A", "B", "C"]
for index, value in enumerate(chunks):
    print(index, value)
print("Ожидалось: 0 A, 1 B, 2 C")
