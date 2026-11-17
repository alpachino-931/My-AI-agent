"""День 15, задания 1–4: try / except и понятные сообщения об ошибках.

Что показывает файл:
1. преобразование текста в int() с обработкой ValueError;
2. сохранение объекта ошибки через `as error`;
3. запрос к GigaChat внутри try / except;
4. короткое сообщение пользователю без длинного технического текста.

Ключ API нигде не печатается.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from gigachat import GigaChat

BASE_DIR = Path(__file__).resolve().parent
CERT_PATH = BASE_DIR / "certs" / "russian_trusted_root_ca_pem (1).crt"

load_dotenv(BASE_DIR.parent / ".env")
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")


def demo_int_conversion() -> None:
    """Задания 1–2: ошибка преобразования и объект ошибки через as error."""
    print("\n--- Задания 1–2. Преобразование текста в int ---")
    text = input("Введите целое число: ").strip()
    try:
        number = int(text)
        print(f"Получилось число: {number}")
    except ValueError as error:
        print("Не удалось преобразовать текст в целое число.")
        print(f"Техническая информация: {error}")


def demo_api_call() -> None:
    """Задания 3–4: запрос к API внутри try / except, короткое сообщение."""
    print("\n--- Задания 3–4. Запрос к API внутри try / except ---")
    prompt = input("Введите запрос к GigaChat: ").strip()
    if not prompt:
        print("Запрос пустой, отправка отменена.")
        return

    try:
        with GigaChat(
            credentials=key,
            scope=scope,
            model="GigaChat-2",
            ca_bundle_file=str(CERT_PATH),
            timeout=60,
        ) as client:
            response = client.chat.create(prompt)
        answer = response.messages[0].content[0].text
        print("Ответ:", answer)
    except Exception:
        print("Не удалось получить ответ")


def print_error_codes() -> None:
    """Задание 9 из теории: типичные коды ошибок API."""
    print("\n--- Типичные коды ошибок API ---")
    codes = [
        (400, "Ошибка в запросе", "некорректные параметры"),
        (401, "Не удалось авторизоваться", "неверный или просроченный токен"),
        (403, "Нет доступа", "недостаточно прав"),
        (413, "Слишком большой запрос", "передано много данных"),
        (422, "Запрос не прошёл проверку", "неверная структура данных"),
        (429, "Слишком много запросов", "превышен лимит запросов"),
        (500, "Ошибка на стороне сервера", "временная проблема сервиса"),
    ]
    for code, meaning, example in codes:
        print(f"{code}: {meaning} — {example}")


if __name__ == "__main__":
    demo_int_conversion()
    demo_api_call()
    print_error_codes()
