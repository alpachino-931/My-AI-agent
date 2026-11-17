"""День 15, задания 5–11: модуль logging и проверка пустого ввода.

Файл настраивает журнал app.log, записывает события уровней INFO, WARNING
и ERROR, логирует этапы запроса к API и не пишет в журнал ключ доступа.
"""

import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from gigachat import GigaChat

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "app.log"
CERT_PATH = BASE_DIR / "certs" / "russian_trusted_root_ca_pem (1).crt"

load_dotenv(BASE_DIR.parent / ".env")
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True,
)
logging.getLogger("httpx").setLevel(logging.WARNING)

logging.info("Программа запущена")
logging.warning("Пример WARNING: подозрительная, но не критическая ситуация")
logging.error("Пример ERROR: API не ответил")
print("В app.log добавлены записи INFO, WARNING и ERROR.")

print("\n--- Задания 10–11. Проверка пустого ввода ---")
text = input("Введите сообщение: ").strip()

if text == "":
    print("Сообщение не должно быть пустым. Запрос не отправлен.")
    logging.warning("Получен пустой ввод")
else:
    try:
        logging.info("Пользовательский запрос получен")
        logging.info("Запрос отправлен в API")
        with GigaChat(
            credentials=key,
            scope=scope,
            model="GigaChat-2",
            ca_bundle_file=str(CERT_PATH),
            timeout=60,
        ) as client:
            response = client.chat.create(text)
        answer = response.messages[0].content[0].text
        logging.info("Ответ успешно получен")
        print("Ответ:", answer)
    except Exception as error:
        logging.error("Ошибка API: %s", error)
        print("Не удалось получить ответ")

print(f"\nЖурнал событий: {LOG_FILE.name}")
