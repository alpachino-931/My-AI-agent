"""День 15, задания 12–19: Pydantic и структурированный ответ chat_parse().

Файл показывает:
- модель Book с полями разных типов и Field(description=...);
- создание объекта вручную и ошибку типа;
- извлечение данных о студенте через chat_parse();
- классификацию сообщения;
- анализ темы;
- смысл strict=True.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from gigachat import GigaChat
from pydantic import BaseModel, Field, ValidationError

BASE_DIR = Path(__file__).resolve().parent
CERT_PATH = BASE_DIR / "certs" / "russian_trusted_root_ca_pem (1).crt"

load_dotenv(BASE_DIR.parent / ".env")
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")


class Book(BaseModel):
    """Задания 12 и 15: простая модель с описаниями полей."""

    title: str = Field(description="Название книги")
    author: str = Field(description="Автор книги")
    year: int = Field(description="Год издания")


class StudentInfo(BaseModel):
    """Задание 16: извлечение данных о студенте."""

    name: str = Field(description="Имя студента")
    group: str = Field(description="Учебная группа")
    score: int = Field(description="Балл от 0 до 100")


class MessageClassification(BaseModel):
    """Задание 17: классификация сообщения."""

    category: str = Field(description="Категория сообщения")
    confidence: int = Field(description="Уверенность в процентах от 0 до 100")


class TopicAnalysis(BaseModel):
    """Задание 18: анализ учебной темы."""

    topic: str = Field(description="Тема вопроса")
    difficulty: str = Field(description="Сложность: низкая, средняя или высокая")
    summary: str = Field(description="Краткое объяснение темы")


def make_client() -> GigaChat:
    return GigaChat(
        credentials=key,
        scope=scope,
        model="GigaChat-2",
        ca_bundle_file=str(CERT_PATH),
        timeout=60,
    )


print("--- Задания 12–13. Модель Book и объект вручную ---")
book = Book(title="Python для начинающих", author="Иванов И. И.", year=2024)
print(book)
print("Название:", book.title)
print("Автор:", book.author)
print("Год:", book.year)

print("\n--- Задание 14. Ошибка типа в Pydantic ---")
try:
    broken = Book(title="Книга", author="Автор", year="не число")
    print(broken)
except ValidationError as error:
    print("Pydantic не принял значение: поле year должно быть целым числом.")
    print("Кратко:", error.errors()[0]["msg"])

print("\n--- Задание 16. Извлечение данных студента через chat_parse ---")
student_prompt = "Извлеки данные из текста: Анна из группы 1ИИ-1 получила 87 баллов."
try:
    with make_client() as client:
        completion, student = client.chat_parse(
            student_prompt,
            response_format=StudentInfo,
            strict=True,
        )
    print("Имя:", student.name)
    print("Группа:", student.group)
    print("Балл:", student.score)
except Exception as error:
    print("Не удалось получить структурированный ответ")
    print("Техническая информация:", error)

print("\n--- Задание 17. Классификация сообщения ---")
classification_prompt = "Классифицируй сообщение: Как исправить ZeroDivisionError в Python?"
try:
    with make_client() as client:
        completion, classification = client.chat_parse(
            classification_prompt,
            response_format=MessageClassification,
            strict=True,
        )
    print("Категория:", classification.category)
    print("Уверенность:", f"{classification.confidence}%")
except Exception as error:
    print("Не удалось получить структурированный ответ")
    print("Техническая информация:", error)

print("\n--- Задание 18. Анализ темы ---")
topic_prompt = "Проанализируй учебную тему: рекурсия в Python."
try:
    with make_client() as client:
        completion, topic = client.chat_parse(
            topic_prompt,
            response_format=TopicAnalysis,
            strict=True,
        )
    print("Тема:", topic.topic)
    print("Сложность:", topic.difficulty)
    print("Кратко:", topic.summary)
except Exception as error:
    print("Не удалось получить структурированный ответ")
    print("Техническая информация:", error)

print("\n--- Задание 19. Зачем нужен strict=True ---")
print("strict=True требует строгого соответствия ответа схеме Pydantic:")
print("все поля обязательны, типы проверяются, лишние вольности не принимаются.")
