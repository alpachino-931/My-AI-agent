"""День 18, звёздочка 1: два набора параметров чанкинга.

Сравнивает 200/40 и 400/80 на всём нормализованном корпусе
и показывает, как меняется количество и средняя длина чанков.
"""

from pathlib import Path

from chunking import split_with_overlap


def collect_chunks(chunk_size: int, overlap: int) -> list[dict]:
    """Собирает чанки всего корпуса для заданных параметров."""
    all_chunks = []
    for file_path in sorted(Path("normalized").glob("*.txt")):
        text = file_path.read_text(encoding="utf-8")
        for chunk_id, chunk in enumerate(split_with_overlap(text, chunk_size, overlap)):
            all_chunks.append({
                "source": file_path.name,
                "chunk_id": chunk_id,
                "length": len(chunk),
                "text": chunk,
            })
    return all_chunks


def main() -> None:
    variants = [
        (200, 40),
        (400, 80),
    ]

    results = {}
    for chunk_size, overlap in variants:
        chunks = collect_chunks(chunk_size, overlap)
        average = sum(chunk["length"] for chunk in chunks) / len(chunks) if chunks else 0
        results[(chunk_size, overlap)] = (chunks, average)
        print(f"chunk_size={chunk_size}, overlap={overlap}")
        print(f"  чанков: {len(chunks)}")
        print(f"  средняя длина: {round(average, 1)}")
        print(f"  минимальная длина: {min((chunk['length'] for chunk in chunks), default=0)}")
        print(f"  максимальная длина: {max((chunk['length'] for chunk in chunks), default=0)}")

    small = results[(200, 40)][0]
    large = results[(400, 80)][0]
    print("\nСравнение:")
    print(f"  200/40 → {len(small)} чанков")
    print(f"  400/80 → {len(large)} чанков")
    if large:
        print(f"  во сколько раз меньше: {round(len(small) / len(large), 2)}")


if __name__ == "__main__":
    main()
