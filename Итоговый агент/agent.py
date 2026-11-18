"""Итоговый ИИ-агент по теме «Поиск ошибок в коде».

Агент объединяет наработки дней 13–19:
1. системную инструкцию (День 13);
2. историю диалога и команды (День 14);
3. обработку ошибок и журнал (День 15);
4. поиск по базе знаний RAG (Дни 16–19).

Схема работы:
    вопрос → поиск похожих чанков → порог релевантности →
    промпт с контекстом → GigaChat → ответ со ссылками на источники.

Запуск:
    python "Итоговый агент/agent.py"
"""

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage, ChatModelOptions

BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent
RAG_DIR = PROJECT_DIR / "19 Эмбеддинги"
CERT_PATH = PROJECT_DIR / "15 Ошибки и Pydantic" / "certs" / "russian_trusted_root_ca_pem (1).crt"
LOG_FILE = BASE_DIR / "agent.log"

MAX_PAIRS = 3
TOP_K = 3
MIN_SCORE = 0.12

# Модуль поиска из Дня 19: embeddings.py, load_chunks(), search().
sys.path.insert(0, str(RAG_DIR))
from embeddings import load_chunks, load_embedder, search  # noqa: E402

SYSTEM_PROMPT = (
    "Ты учебный ИИ-помощник по языку Python. Тема — поиск и исправление ошибок в коде. "
    "Отвечай на русском языке кратко и по делу. Опирайся только на фрагменты базы знаний, "
    "которые переданы в сообщении пользователя. Если во фрагментах нет ответа, честно скажи, "
    "что в базе знаний нет подходящей информации, и не придумывай факты."
)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True,
)
logging.getLogger("httpx").setLevel(logging.WARNING)


def trim_history(history: list[ChatMessage], max_pairs: int = MAX_PAIRS) -> list[ChatMessage]:
    """Оставляет системную инструкцию и последние max_pairs обменов."""
    system = history[0]
    dialogue = history[1:]
    return [system] + dialogue[-max_pairs * 2:]


def build_context(results: list[dict]) -> str:
    """Собирает найденные чанки в текст с номерами источников."""
    parts = []
    for number, item in enumerate(results, start=1):
        parts.append(
            f"[{number}] {item['source']}, chunk_id={item['chunk_id']}, "
            f"score={item['score']:.4f}\n{item['text']}"
        )
    return "\n\n".join(parts)


def show_history(history: list[ChatMessage]) -> None:
    """Показывает роли сообщений без полного текста."""
    print(f"Сообщений в истории: {len(history)}")
    for number, message in enumerate(history):
        content = message.content
        if isinstance(content, list):
            content = content[0].text if content else ""
        preview = str(content).replace("\n", " ")[:60]
        print(f"  {number}. {message.role}: {preview}")


def main() -> None:
    logging.info("Старт итогового агента")

    load_dotenv(PROJECT_DIR / ".env")
    key = os.getenv("GIGACHAT_CREDENTIALS")
    scope = os.getenv("GIGACHAT_SCOPE")
    if not key:
        logging.error("Не найден GIGACHAT_CREDENTIALS")
        print("Не найден ключ API. Проверьте файл .env в корне проекта.")
        sys.exit(1)

    print("Итоговый ИИ-агент: поиск ошибок в коде.")
    print("Вопрос ищется в базе знаний, затем GigaChat объясняет ответ.")
    print("Команды: выход | очистить | история\n")

    embedder = load_embedder()
    chunks = load_chunks(
        str(RAG_DIR / "chunks"),
        str(RAG_DIR / "chunks_summary.csv"),
    )
    if not chunks:
        logging.error("База знаний пуста")
        print("База знаний пуста. Проверьте папку 19 Эмбеддинги/chunks.")
        sys.exit(1)

    chunk_embeddings = embedder.encode([chunk["text"] for chunk in chunks])
    print(f"База знаний: {len(chunks)} фрагментов, модель: {embedder.name}")
    print(f"Порог релевантности: {MIN_SCORE}\n")

    messages = [ChatMessage(role="system", content=SYSTEM_PROMPT)]
    exchanges = 0

    with GigaChat(
        credentials=key,
        scope=scope,
        model="GigaChat-2",
        ca_bundle_file=str(CERT_PATH),
        timeout=60,
    ) as client:
        while True:
            try:
                raw = input("Вы: ")
            except (EOFError, KeyboardInterrupt):
                print("\nДиалог завершён.")
                break

            user_text = raw.strip()
            command = user_text.lower()

            if command in ("выход", "exit", "quit"):
                print("Диалог завершён.")
                break

            # Пустой запрос не отправляется ни в поиск, ни в модель.
            if not user_text:
                logging.warning("Получен пустой ввод")
                print("Запрос пустой. Введите вопрос по Python, например: "
                      "«Почему возникает NameError?»")
                continue

            if command == "очистить":
                messages = messages[:1]
                print("История диалога очищена. Системная инструкция сохранена.")
                continue

            if command == "история":
                show_history(messages)
                continue

            # Шаг 1. Поиск по базе знаний.
            results = search(embedder, chunks, chunk_embeddings, user_text, top_k=TOP_K)
            best = results[0]
            logging.info("Поиск выполнен: %s#%s score=%.4f",
                         best["source"], best["chunk_id"], best["score"])

            if best["score"] < MIN_SCORE:
                logging.warning("Нет подходящего фрагмента: score=%.4f", best["score"])
                print(f"В базе знаний нет подходящего фрагмента "
                      f"(лучший score {best['score']:.4f} < порога {MIN_SCORE}).")
                print("Попробуйте переформулировать вопрос по теме Python.")
                continue

            # Шаг 2. Промпт с контекстом и вопросом.
            context = build_context(results)
            prompt = (
                f"Вопрос пользователя: {user_text}\n\n"
                f"Фрагменты базы знаний:\n{context}\n\n"
                "Ответь по этим фрагментам. Не перечисляй источники в ответе — "
                "программа выведет их отдельным списком."
            )
            messages.append(ChatMessage(role="user", content=prompt))

            # Шаг 3. Запрос к GigaChat.
            request = ChatCompletionRequest(
                model="GigaChat-2",
                messages=messages,
                model_options=ChatModelOptions(
                    temperature=0.2,
                    max_tokens=500,
                    repetition_penalty=1.05,
                ),
            )

            try:
                response = client.chat.create(request)
                answer = response.messages[0].content[0].text
            except Exception as error:
                logging.error("Ошибка API: %s", error)
                messages.pop()
                print("Не удалось получить ответ от GigaChat. Попробуйте позже.")
                continue

            print(f"\nПомощник: {answer}\n")
            print("Источники:")
            for number, item in enumerate(results, start=1):
                print(f"  [{number}] {item['source']}, chunk_id={item['chunk_id']}, "
                      f"score={item['score']:.4f}")
            print()

            messages.append(ChatMessage(role="assistant", content=answer))
            messages = trim_history(messages)
            exchanges += 1
            logging.info("Ответ получен, обменов за запуск: %d", exchanges)

    print(f"Успешных ответов за запуск: {exchanges}")
    print(f"Журнал событий: {LOG_FILE.name}")


if __name__ == "__main__":
    main()
