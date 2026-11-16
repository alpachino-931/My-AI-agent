import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import (
    ChatCompletionRequest,
    ChatMessage,
    ChatModelOptions,
)
from prompts import SYSTEM_PROMPT

# 1. Чтение настроек: получение ключа, scope и пути к сертификату из .env
CERT_PATH = Path(__file__).resolve().parent / "certs" / "russian_trusted_root_ca_pem (1).crt"
load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")

print("--- Настройка запроса ---")

# 2. Ввод пользователя: сбор исходных данных с удалением пробелов
print("Введите ваш код и текст ошибки (обязательно):")
user_code = input("> ").strip()

if not user_code:
    print("Ошибка: Поле с кодом и ошибкой не может быть пустым. Запрос не отправлен.")
    sys.exit(0)

constraint = input("Введите ограничения (например, 'без сторонних библиотек') или нажмите Enter: ").strip()
if not constraint:
    constraint = "Не указано"

desired_result = input("Опишите желаемый результат (что должно работать): ").strip()
if not desired_result:
    desired_result = "Исправить ошибку"

print("\nВыберите формат ответа:")
print("1 - Краткий (только причина и исправленный код)")
print("2 - Пошаговый (подробное объяснение и шаги)")
format_choice = input("Ваш выбор (1 или 2): ").strip()

if format_choice == "1":
    format_instruction = "Ответ должен быть кратким: только причина ошибки и исправленный код без лишних объяснений."
elif format_choice == "2":
    format_instruction = "Ответ должен быть подробным: объясни причину, покажи исправленный код и напиши совет, как избежать ошибки."
else:
    print("Ошибка: Неверный выбор формата. Нужно ввести 1 или 2. Запрос не отправлен.")
    sys.exit(0)

user_prompt = f"""Язык программирования: Python (если не указано иное).
Код и ошибка:
{user_code}

Ограничения: {constraint}
Желаемый результат: {desired_result}
Формат ответа: {format_instruction}
"""

print("\n--- Сформированный запрос (user_prompt) ---")
print(user_prompt)
print("-------------------------------------------\n")

# 3. Системная инструкция: передача базовых правил из prompts.py
messages = [
    ChatMessage(role="system", content=SYSTEM_PROMPT),
    ChatMessage(role="user", content=user_prompt),
]

# 4. Сборка и отправка запроса: добавление ChatModelOptions и отправка в API
request = ChatCompletionRequest(
    model="GigaChat-2",
    messages=messages,
    model_options=ChatModelOptions(
        temperature=0.2,
        max_tokens=400,
        repetition_penalty=1.05
    )
)

print("Отправляем запрос...")
with GigaChat(
    credentials=key,
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file=str(CERT_PATH),
    timeout=60,
) as client:
    response = client.chat.create(request)

# 5. Извлечение текста ответа: вытаскиваем чистый текст из объекта ответа API
answer = response.messages[0].content[0].text
print("\n--- Ответ ассистента ---")
print(answer)
print("------------------------\n")

with open("last_prompt.txt", "w", encoding="utf-8") as f:
    f.write(user_prompt)

with open("last_answer.txt", "w", encoding="utf-8") as f:
    f.write(answer)

print("Промпт сохранен в last_prompt.txt, ответ сохранен в last_answer.txt")