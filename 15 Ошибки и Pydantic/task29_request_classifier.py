"""День 15, задание 29: классификатор обращения.

Модель содержит category, priority и summary. Все ошибки API попадают
в app.log, пользователь видит короткое сообщение.
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


class RequestClassification(BaseModel):
    category: str = Field(description="Категория обращения")
    priority: str = Field(description="Приоритет: низкий, средний или высокий")
    summary: str = Field(description="Краткая суть обращения")


def main() -> None:
    logging.info("task29: старт")
    load_dotenv(BASE_DIR.parent / ".env")
    key = os.getenv("GIGACHAT_CREDENTIALS")
    scope = os.getenv("GIGACHAT_SCOPE")

    text = input("Введите текст обращения: ").strip()
    if not text:
        logging.warning("task29: пустой ввод")
        print("Обращение не должно быть пустым.")
        return

    try:
        logging.info("task29: запрос отправлен")
        with GigaChat(
            credentials=key,
            scope=scope,
            model="GigaChat-2",
            ca_bundle_file=str(CERT_PATH),
            timeout=60,
        ) as client:
            completion, parsed = client.chat_parse(
                f"Классифицируй обращение: {text}",
                response_format=RequestClassification,
                strict=True,
            )
        logging.info("task29: ответ получен")
        print("Категория:", parsed.category)
        print("Приоритет:", parsed.priority)
        print("Кратко:", parsed.summary)
    except Exception as error:
        logging.error("task29: ошибка API: %s", error)
        print("Не удалось обработать обращение")


if __name__ == "__main__":
    main()
