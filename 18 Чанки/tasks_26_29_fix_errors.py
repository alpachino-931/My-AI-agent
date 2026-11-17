"""День 18, задания 26–29: исправление ошибок."""

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chunk_size = 10

print("--- Задание 26. Ошибка range ---")
chunks = []
for start in range(0, len(text), chunk_size):
    chunks.append(text[start:start + chunk_size])
print(chunks)

print("\n--- Задание 27. Ошибка step ---")
overlap = 3
step = chunk_size - overlap
print("step =", step)

print("\n--- Задание 28. Ошибка enumerate ---")
chunks = ["A", "B", "C"]
for chunk_id, chunk in enumerate(chunks):
    print(chunk_id, chunk)

print("\n--- Задание 29. Ошибка имени файла ---")
file_name = "python.txt"
chunk_id = 1
filename = file_name[:-4] + "_chunk_" + str(chunk_id) + ".txt"
print(filename)
