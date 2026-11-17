"""Функции разбиения текста на чанки для дня 18."""


def split_into_chunks(text: str, chunk_size: int) -> list[str]:
    """Простое разбиение по символам без перекрытия."""
    if chunk_size <= 0:
        raise ValueError("chunk_size должен быть больше 0")
    chunks = []
    for start in range(0, len(text), chunk_size):
        chunks.append(text[start:start + chunk_size])
    return chunks


def split_with_overlap(
    text: str,
    chunk_size: int,
    overlap: int,
    minimum_length: int = 30,
) -> list[str]:
    """Разбиение с перекрытием, обрезкой краёв и отбрасыванием коротких чанков."""
    if chunk_size <= 0:
        raise ValueError("chunk_size должен быть больше 0")
    if overlap < 0:
        raise ValueError("overlap не может быть отрицательным")
    if overlap >= chunk_size:
        raise ValueError("overlap должен быть меньше chunk_size")

    chunks = []
    step = chunk_size - overlap
    for start in range(0, len(text), step):
        chunk = text[start:start + chunk_size].strip()
        if len(chunk) >= minimum_length:
            chunks.append(chunk)
    return chunks
