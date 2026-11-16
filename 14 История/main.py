"""ИИ-помощник по поиску и исправлению ошибок в коде.

День 14: диалог с историей. Пользователь задаёт вопросы без перезапуска
программы, помощник помнит предыдущие реплики в пределах текущего запуска.

Команды:
    выход   — завершить работу;
    очистить — удалить историю диалога, оставив системную инструкцию;
    история — показать количество сообщений и их роли.
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import (
    ChatCompletionRequest,
    ChatMessage,
    ChatModelOptions,
)
from prompts import SYSTEM_PROMPT

CERT_PATH = Path(__file__).resolve().parent / "certs" / "russian_trusted_root_ca_pem (1).crt"
HISTORY_FILE = Path(__file__).resolve().parent / "chat_history.txt"
MAX_PAIRS = 3

load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")


def trim_history(history: list[ChatMessage], max_pairs: int = MAX_PAIRS) -> list[ChatMessage]:
    """Оставляет system и последние max_pairs полных обменов user/assistant."""
    limit = 1 + 2 * max_pairs
    if len(history) <= limit:
        return history
    return [history[0]] + history[-2 * max_pairs:]


def show_history(history: list[ChatMessage]) -> None:
    """Показывает размер истории и роли сообщений, не меняя список."""
    print(f"Сообщений в истории: {len(history)}")
    for number, message in enumerate(history, start=1):
        print(f"  {number}. {message.role}")


def log_exchange(user_text: str, answer_text: str) -> None:
    """Дописывает завершённый обмен в текстовый журнал."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as log:
        log.write(f"Пользователь: {user_text}\n")
        log.write(f"Помощник: {answer_text}\n\n")


# Системная инструкция создаётся один раз и остаётся первым сообщением.
messages = [ChatMessage(role="system", content=SYSTEM_PROMPT)]
exchanges = 0

with open(HISTORY_FILE, "a", encoding="utf-8") as log:
    log.write("=== Новый запуск ===\n\n")

print("ИИ-помощник по поиску ошибок в коде. Диалог с историей.")
print("Опишите код и ошибку одной репликой, затем задавайте уточнения.")
print("Команды: выход | очистить | история\n")

print("Отправляем запрос...")

with GigaChat(
    credentials=key,
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file=str(CERT_PATH),
    timeout=60,
) as client:
    while True:
        raw = input("Вы: ")
        user_text = raw.strip()
        command = user_text.lower()

        # Сначала команды и пустой ввод — до обращения к модели.
        if command in ("выход", "exit", "quit"):
            print("Диалог завершён.")
            break

        if not user_text:
            print("Введите текст: код и ошибку или уточняющий вопрос.")
            continue

        if command == "очистить":
            messages = [messages[0]]
            print("История текущего диалога очищена. Продолжаем с системной инструкцией.")
            with open(HISTORY_FILE, "a", encoding="utf-8") as log:
                log.write("[История текущего диалога очищена]\n\n")
            continue

        if command == "история":
            show_history(messages)
            continue

        # Обычная реплика: сохраняем исходный регистр текста.
        messages.append(ChatMessage(role="user", content=user_text))

        request = ChatCompletionRequest(
            model="GigaChat-2",
            messages=messages,
            model_options=ChatModelOptions(
                temperature=0.2,
                max_tokens=400,
                repetition_penalty=1.05,
            ),
        )

        response = client.chat.create(request)
        answer = response.messages[0].content[0].text

        print(f"Помощник: {answer}")
        messages.append(ChatMessage(role="assistant", content=answer))
        exchanges += 1

        # Сокращаем историю только после успешного ответа.
        messages = trim_history(messages)
        print(f"[В истории сообщений: {len(messages)}, обменов за запуск: {exchanges}]")

        log_exchange(user_text, answer)

print(f"Успешных обменов за запуск: {exchanges}")
print(f"Журнал диалога сохранён в {HISTORY_FILE.name}")
