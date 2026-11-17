"""День 15, задание 30: надёжный LLM-анализатор ошибок в коде.

Программа:
1. безопасно получает ключ из .env (ключ не печатается и не логируется);
2. настраивает logging в app.log;
3. получает текст пользователя и удаляет пробелы по краям;
4. не отправляет пустой запрос;
5. использует Pydantic-модель из шести полей;
6. получает структурированный ответ через chat_parse(strict=True);
7. выводит отдельные поля и сохраняет их в result.txt;
8. пишет INFO, WARNING и ERROR в журнал;
9. перехватывает ошибку API и показывает короткое сообщение.
"""

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from gigachat import GigaChat
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "app.log"
RESULT_FILE = BASE_DIR / "result.txt"
CERT_PATH = BASE_DIR / "certs" / "russian_trusted_root_ca_pem (1).crt"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True,
)
logging.getLogger("httpx").setLevel(logging.WARNING)


class CodeErrorAnalysis(BaseModel):
    """Структура ответа: шесть обязательных полей."""

    language: str = Field(description="Язык программирования")
    error_type: str = Field(description="Тип ошибки, например ZeroDivisionError")
    severity: str = Field(description="Критичность: низкая, средняя или высокая")
    cause: str = Field(description="Причина ошибки простыми словами")
    fix: str = Field(description="Как исправить ошибку")
    advice: str = Field(description="Совет, как избежать ошибки в будущем")


def main() -> None:
    logging.info("Старт программы")

    # Задание 9: ключ только читается из окружения, в лог и на экран не попадает.
    load_dotenv(BASE_DIR.parent / ".env")
    key = os.getenv("GIGACHAT_CREDENTIALS")
    scope = os.getenv("GIGACHAT_SCOPE")

    if not key:
        logging.error("Не найден GIGACHAT_CREDENTIALS")
        print("Не найден ключ API. Проверьте файл .env.")
        sys.exit(1)

    print("Анализатор ошибок в коде (структурированный ответ).")
    print("Введите одной строкой код и текст ошибки.")
    text = input("> ").strip()

    if text == "":
        logging.warning("Получен пустой ввод")
        print("Сообщение не должно быть пустым. Запрос не отправлен.")
        return

    logging.info("Пользовательский текст получен")
    prompt = (
        "Проанализируй ошибку в коде. Верни язык, тип ошибки, критичность, "
        "причину, способ исправления и совет.\n"
        f"Данные пользователя: {text}"
    )
    logging.info("Промпт сформирован")

    successes = 0
    try:
        logging.info("Запрос отправлен в API")
        with GigaChat(
            credentials=key,
            scope=scope,
            model="GigaChat-2",
            ca_bundle_file=str(CERT_PATH),
            timeout=60,
        ) as client:
            completion, parsed = client.chat_parse(
                prompt,
                response_format=CodeErrorAnalysis,
                strict=True,
            )

        successes += 1
        logging.info("Структурированный ответ получен")

        print("\n--- Результат ---")
        print("Язык:", parsed.language)
        print("Тип ошибки:", parsed.error_type)
        print("Критичность:", parsed.severity)
        print("Причина:", parsed.cause)
        print("Исправление:", parsed.fix)
        print("Совет:", parsed.advice)

        with open(RESULT_FILE, "w", encoding="utf-8") as result_file:
            result_file.write(f"Язык: {parsed.language}\n")
            result_file.write(f"Тип ошибки: {parsed.error_type}\n")
            result_file.write(f"Критичность: {parsed.severity}\n")
            result_file.write(f"Причина: {parsed.cause}\n")
            result_file.write(f"Исправление: {parsed.fix}\n")
            result_file.write(f"Совет: {parsed.advice}\n")
        logging.info("Результат сохранён в result.txt")
        print(f"\nРезультат сохранён в {RESULT_FILE.name}")
    except Exception as error:
        logging.error("Ошибка structured output: %s", error)
        print("Не удалось получить структурированный ответ. Попробуйте позже.")

    print(f"Успешных запросов за запуск: {successes}")
    print(f"Журнал событий: {LOG_FILE.name}")


if __name__ == "__main__":
    main()
