"""День 15, задание 28: извлечение данных о студенте.

Свободный текст превращается в Pydantic-объект с полями name, group, score.
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


class StudentInfo(BaseModel):
    name: str = Field(description="Имя студента")
    group: str = Field(description="Учебная группа")
    score: int = Field(description="Балл от 0 до 100")


def main() -> None:
    logging.info("task28: старт")
    load_dotenv(BASE_DIR.parent / ".env")
    key = os.getenv("GIGACHAT_CREDENTIALS")
    scope = os.getenv("GIGACHAT_SCOPE")

    text = input("Введите текст о студенте: ").strip()
    if not text:
        logging.warning("task28: пустой ввод")
        print("Текст не должен быть пустым.")
        return

    try:
        logging.info("task28: запрос отправлен")
        with GigaChat(
            credentials=key,
            scope=scope,
            model="GigaChat-2",
            ca_bundle_file=str(CERT_PATH),
            timeout=60,
        ) as client:
            completion, parsed = client.chat_parse(
                f"Извлеки данные о студенте из текста: {text}",
                response_format=StudentInfo,
                strict=True,
            )
        logging.info("task28: ответ получен")
        print("Имя:", parsed.name)
        print("Группа:", parsed.group)
        print("Балл:", parsed.score)
    except Exception as error:
        logging.error("task28: ошибка API: %s", error)
        print("Не удалось получить структурированный ответ")


if __name__ == "__main__":
    main()
