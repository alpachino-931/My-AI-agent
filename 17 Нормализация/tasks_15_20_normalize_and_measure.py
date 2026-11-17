"""День 17, задания 15–20: normalize_text(), пустой текст и измерения."""

from pathlib import Path

from text_normalization import normalize_text

print("--- Задание 15. Функция normalize_text() ---")
dirty = Path("dirty_instruction.txt").read_text(encoding="utf-8")
print("Исходный текст:")
print(dirty)
print("\nНормализованный текст:")
print(normalize_text(dirty))

print("\n--- Задание 16. Проверка функции на грязном тексте ---")
print("Строк до: ", len(dirty.splitlines()))
print("Строк после:", len(normalize_text(dirty).splitlines()))

print("\n--- Задание 17. Текст из одних пробелов ---")
print("Результат:", repr(normalize_text("   \n\t\n   ")))

print("\n--- Задания 18–20. До, после, разница и процент ---")
before = len(dirty)
after = len(normalize_text(dirty))
removed = before - after
percent = removed / before * 100 if before else 0
print("До:", before)
print("После:", after)
print("Удалено символов:", removed)
print("Сокращение:", round(percent, 1), "%")
