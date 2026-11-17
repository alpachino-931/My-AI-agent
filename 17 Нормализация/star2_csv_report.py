"""День 17, звёздочка 2: CSV-отчёт по нормализации корпуса."""

import csv
from pathlib import Path

from text_normalization import normalize_text

rows = []
for file_path in sorted(Path("cleaned").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    after = len(normalize_text(text))
    before = len(text)
    percent = (before - after) / before * 100 if before else 0.0
    rows.append({
        "source": file_path.name,
        "before": before,
        "after": after,
        "reduction_percent": round(percent, 1),
    })

with open("corpus_report.csv", "w", encoding="utf-8", newline="") as report:
    writer = csv.DictWriter(report, fieldnames=["source", "before", "after", "reduction_percent"])
    writer.writeheader()
    writer.writerows(rows)

print("CSV-отчёт создан: corpus_report.csv")
for row in rows:
    print(row)
