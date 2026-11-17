"""День 17, звёздочка 3: список файлов короче 50 символов после очистки."""

from pathlib import Path

from text_normalization import normalize_text

short_files = []
for file_path in sorted(Path("cleaned").glob("*.txt")):
    text = file_path.read_text(encoding="utf-8")
    after = normalize_text(text)
    if len(after) < 50:
        short_files.append(file_path.name)

if short_files:
    print("Файлы короче 50 символов:", ", ".join(short_files))
else:
    print("Файлов короче 50 символов нет.")
