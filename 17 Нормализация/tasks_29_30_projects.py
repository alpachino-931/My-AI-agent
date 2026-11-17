"""День 17, задания 29–30: очистка инструкции и нормализация корпуса."""

from pathlib import Path

from text_normalization import normalize_text

print("--- Задание 29. Очистка учебной инструкции ---")
source = Path("dirty_instruction.txt")
dirty = source.read_text(encoding="utf-8")
cleaned = normalize_text(dirty, drop_service_lines=True)
Path("cleaned_instruction.txt").write_text(cleaned, encoding="utf-8")

print("До:", len(dirty), "символов")
print("После:", len(cleaned), "символов")
print("Результат:")
print(cleaned)

print("\n--- Задание 30. Нормализация корпуса Дня 16 ---")
normalized_dir = Path("normalized")
normalized_dir.mkdir(exist_ok=True)
files = sorted(Path("cleaned").glob("*.txt"))
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    (normalized_dir / file_path.name).write_text(normalize_text(text), encoding="utf-8")
print("Обработано документов:", len(files))
print("Нормализованные файлы сохранены в normalized")
