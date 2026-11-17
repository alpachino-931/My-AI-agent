"""Общие функции очистки и нормализации текста для дня 17."""

SERVICE_LINES = {"черновик", "служебная копия"}


def clean_line(line: str) -> str:
    """Убирает неразрывные пробелы, табуляции и лишние пробелы в строке."""
    line = line.replace("\u00a0", " ")
    line = line.replace("\t", " ")
    return " ".join(line.split())


def normalize_text(text: str, drop_service_lines: bool = False) -> str:
    """Очищает строки, убирает пустые и точные дубли, сохраняя порядок."""
    clean_lines = []
    for line in text.splitlines():
        line = clean_line(line)
        if line == "":
            continue
        if drop_service_lines and line.lower() in SERVICE_LINES:
            continue
        if line not in clean_lines:
            clean_lines.append(line)
    return "\n".join(clean_lines)


def normalize_text_case_insensitive(text: str) -> str:
    """Удаляет дубли без учёта регистра, сохраняя первый исходный вариант."""
    clean_lines = []
    seen = set()
    for line in text.splitlines():
        line = clean_line(line)
        if line == "":
            continue
        key = line.lower()
        if key in seen:
            continue
        seen.add(key)
        clean_lines.append(line)
    return "\n".join(clean_lines)
