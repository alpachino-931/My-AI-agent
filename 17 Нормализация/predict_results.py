"""День 17, уровень 9: предсказание результата."""

print("--- Предсказание 1 ---")
text = "  A   B  "
print(repr(" ".join(text.split())))
print("Ожидалось: 'A B'")

print("\n--- Предсказание 2 ---")
line = "\tPython\t"
print(repr(line.strip()))
print("Ожидалось: 'Python'")

print("\n--- Предсказание 3 ---")
lines = ["A", "A", "B"]
unique = []
for item in lines:
    if item not in unique:
        unique.append(item)
print(unique)
print("Ожидалось: ['A', 'B']")
