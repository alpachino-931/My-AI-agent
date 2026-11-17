"""День 17, задания 21–24: папка normalized и обработка всего корпуса."""

from pathlib import Path

from text_normalization import normalize_text

print("--- Задание 21. Папка normalized ---")
normalized_dir = Path("normalized")
normalized_dir.mkdir(exist_ok=True)
print("Папка существует:", normalized_dir.exists())

print("\n--- Задания 22–24. Все файлы, имена и сводка ---")
files = sorted(Path("cleaned").glob("*.txt"))
print("Документ                 До    После")
print("-" * 40)

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    normalized = normalize_text(text)
    (normalized_dir / file_path.name).write_text(normalized, encoding="utf-8")
    print(f"{file_path.name:<24}{len(text):>5}{len(normalized):>8}")

print(f"\nОбработано файлов: {len(files)}")
print("Имена сохранены:", sorted(p.name for p in normalized_dir.glob("*.txt")) == [p.name for p in files])
