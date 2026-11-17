"""День 17, задание 31: итоговая подготовка чистого корпуса для чанкинга.

Программа:
1. находит все TXT-файлы в cleaned/;
2. заменяет неразрывные пробелы и табуляции;
3. убирает лишние пробелы внутри строк;
4. удаляет пустые строки и точные дубли строк;
5. сохраняет исходный регистр текста;
6. создаёт папку normalized/ и сохраняет файлы под теми же именами;
7. выводит размер до и после, общий объём и процент сокращения;
8. проверяет, что после очистки не появилось пустых документов;
9. пишет CSV-отчёт и список коротких файлов (задания со звёздочкой).
"""

import csv
import os
from pathlib import Path

from text_normalization import normalize_text

os.chdir(os.path.dirname(os.path.abspath(__file__)))

SOURCE_DIR = Path("cleaned")
OUTPUT_DIR = Path("normalized")
CSV_FILE = Path("corpus_report.csv")
SHORT_LIMIT = 50

OUTPUT_DIR.mkdir(exist_ok=True)

files = sorted(SOURCE_DIR.glob("*.txt"))
if not files:
    print("В папке cleaned нет TXT-файлов.")
    raise SystemExit(1)

rows = []
short_files = []
total_before = 0
total_after = 0

print("Документ                 До    После  Сокращение")
print("-" * 52)

for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    normalized = normalize_text(text)

    (OUTPUT_DIR / file_path.name).write_text(normalized, encoding="utf-8")

    before = len(text)
    after = len(normalized)
    percent = (before - after) / before * 100 if before else 0.0

    total_before += before
    total_after += after
    rows.append({
        "source": file_path.name,
        "before": before,
        "after": after,
        "reduction_percent": round(percent, 1),
    })

    if after < SHORT_LIMIT:
        short_files.append(file_path.name)

    print(f"{file_path.name:<24}{before:>5}{after:>8}{percent:>10.1f}%")

total_percent = (total_before - total_after) / total_before * 100 if total_before else 0.0

print("-" * 52)
print(f"{'Всего':<24}{total_before:>5}{total_after:>8}{total_percent:>10.1f}%")
print(f"Документов обработано: {len(files)}")
print(f"Общий объём до: {total_before} символов")
print(f"Общий объём после: {total_after} символов")
print(f"Процент сокращения: {round(total_percent, 1)}%")

empty_files = [path.name for path in OUTPUT_DIR.glob("*.txt") if path.read_text(encoding="utf-8").strip() == ""]
print(f"Пустых документов после очистки: {len(empty_files)}")
if empty_files:
    print("Проверьте файлы:", ", ".join(empty_files))

with open(CSV_FILE, "w", encoding="utf-8", newline="") as report:
    writer = csv.DictWriter(report, fieldnames=["source", "before", "after", "reduction_percent"])
    writer.writeheader()
    writer.writerows(rows)

print(f"\nCSV-отчёт сохранён в {CSV_FILE.name}")
if short_files:
    print("Файлы короче 50 символов:", ", ".join(short_files))
else:
    print("Файлов короче 50 символов нет.")
