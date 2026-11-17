"""День 18, задания 1–8: простое разбиение и overlap."""

from chunking import split_into_chunks, split_with_overlap

print("--- Задание 1. Строка по 10 символов ---")
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123"
print(split_into_chunks(text, 10))

print("\n--- Задание 2. chunk_size = 7 ---")
print(split_into_chunks(text, 7))

print("\n--- Задание 3. Последний чанк ---")
last = split_into_chunks(text, 7)[-1]
print("Последний чанк:", last, "длина:", len(last))

print("\n--- Задание 4. Функция split_into_chunks() ---")
print(split_into_chunks("Python — язык программирования.", 10))

print("\n--- Задание 5. Шаг при overlap ---")
chunk_size, overlap = 100, 20
print("step =", chunk_size - overlap)

print("\n--- Задание 6. Разбиение с overlap 20/5 ---")
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(split_with_overlap(text, 20, 5, minimum_length=0))

print("\n--- Задание 7. Сравнение без overlap и с overlap ---")
print("Без overlap:", split_into_chunks(text, 20))
print("С overlap: ", split_with_overlap(text, 20, 5, minimum_length=0))

print("\n--- Задание 8. Ошибочный overlap ---")
try:
    split_with_overlap(text, 20, 20)
except ValueError as error:
    print("Ошибка перехвачена:", error)
