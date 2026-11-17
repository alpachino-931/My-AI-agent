"""День 15, задание 27: анализатор учебного вопроса.

Пользователь вводит учебный вопрос, программа получает структурированный
ответ (тема, сложность, краткий ответ) и пишет события в app.log.
"""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from gigachat import GigaChat
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "app.log"
CERT_PATH = BASE_DIR / "certs" / "russian_trusted_root_ca_pem (1).crt"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True,
)
logging.getLogger("httpx").setLevel(logging.WARNING)


class QuestionAnalysis(BaseModel):
    topic: str = Field(description="Учебная тема вопроса")
    difficulty: str = Field(description="Сложность: низкая, средняя или высокая")
    short_answer: str = Field(description="Краткий ответ на вопрос")


def main() -> None:
    logging.info("task27: старт")
    load_dotenv(BASE_DIR.parent / ".env")
    key = os.getenv("GIGACHAT_CREDENTIALS")
    scope = os.getenv("GIGACHAT_SCOPE")

    question = input("Введите учебный вопрос: ").strip()
    if not question:
        logging.warning("task27: пустой ввод")
        print("Вопрос не должен быть пустым.")
        return

    try:
        logging.info("task27: запрос отправлен")
        with GigaChat(
            credentials=key,
            scope=scope,
            model="GigaChat-2",
            ca_bundle_file=str(CERT_PATH),
            timeout=60,
        ) as client:
            completion, parsed = client.chat_parse(
                f"Проанализируй учебный вопрос: {question}",
                response_format=QuestionAnalysis,
                strict=True,
            )
        logging.info("task27: ответ получен")
        print("Тема:", parsed.topic)
        print("Сложность:", parsed.difficulty)
        print("Краткий ответ:", parsed.short_answer)
    except Exception as error:
        logging.error("task27: ошибка API: %s", error)
        print("Не удалось получить ответ")


if __name__ == "__main__":
    main()
