import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage
from prompts import SYSTEM_PROMPT

CERT_PATH = Path(__file__).resolve().parent / "certs" / "russian_trusted_root_ca_pem (1).crt"
load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")

question = input("Какой у вас вопрос? ").strip()

# ПРОВЕРКА ПУСТОГО ВВОДА
# Если после .strip() ничего не осталось — это пустая строка или одни пробелы.
# До GigaChat не доходим: выводим понятное сообщение и выходим.
if not question:
    print("Поле пустое. Вставьте код и текст ошибки, чтобы я мог помочь.")
    sys.exit(0)
    
messages = [
    ChatMessage(
        role="system",
        content=SYSTEM_PROMPT,
    ),
    ChatMessage(
        role="user",
        content=question,
    ),
]

# Собираем запрос из сообщений
request = ChatCompletionRequest(
    model="GigaChat-2",
    messages=messages,
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

answer = response.messages[0].content[0].text
print("Ответ:")
print(answer)