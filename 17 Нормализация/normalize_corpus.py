"""День 17, раздел 36: нормализация всего корпуса.

Читает TXT-файлы из cleaned/, очищает их и сохраняет в normalized/
под теми же именами, выводит размер до и после.
"""

import os
from pathlib import Path

from text_normalization import normalize_text

os.chdir(os.path.dirname(os.path.abspath(__file__)))

source_dir = Path("cleaned")
normalized_dir = Path("normalized")
normalized_dir.mkdir(exist_ok=True)

files = sorted(source_dir.glob("*.txt"))

print("Файлов в исходной папке:", len(files))
for file_path in files:
    text = file_path.read_text(encoding="utf-8")
    normalized = normalize_text(text)
    output_path = normalized_dir / file_path.name
    output_path.write_text(normalized, encoding="utf-8")
    print(f"{file_path.name:<24} {len(text):>4} → {len(normalized):>4}")

print("Готово: нормализованные файлы лежат в папке normalized")
