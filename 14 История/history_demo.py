"""Демонстрация истории диалога без обращения к API.

Скрипт показывает:
1. как выглядит список messages из ролей system / user / assistant;
2. как растёт длина истории после каждого обмена;
3. как работают команды, пустой ввод и цикл диалога;
4. как ограничивается размер истории (system + последние max_pairs пар).

Модель GigaChat здесь не вызывается: вместо ответа подставляется
тестовый текст «Тестовый ответ без API».
"""

from gigachat.models import ChatMessage
from prompts import SYSTEM_PROMPT

MAX_PAIRS = 3


def show_history(messages: list[ChatMessage], title: str) -> None:
    """Печатает длину списка и роли сообщений по порядку."""
    print(f"\n{title}")
    print(f"Длина messages: {len(messages)}")
    for number, message in enumerate(messages, start=1):
        print(f"  {number}. {message.role}")


def message_text(message: ChatMessage) -> str:
    """Возвращает текст сообщения (в этой версии gigachat content — список частей)."""
    content = message.content
    if isinstance(content, str):
        return content
    return "".join(part.text or "" for part in content)


def trim_history(messages: list[ChatMessage], max_pairs: int = MAX_PAIRS) -> list[ChatMessage]:
    """Оставляет system и последние max_pairs полных обменов."""
    limit = 1 + 2 * max_pairs
    if len(messages) <= limit:
        return messages
    return [messages[0]] + messages[-2 * max_pairs:]


print("=== 1. История после одного обмена (без API) ===")
messages = [
    ChatMessage(role="system", content=SYSTEM_PROMPT),
    ChatMessage(
        role="user",
        content="У меня ZeroDivisionError: division by zero. Код: x = 10 / 0",
    ),
    ChatMessage(
        role="assistant",
        content="Тестовый ответ без API: деление на ноль нужно проверять до операции.",
    ),
]
show_history(messages, "Один полный обмен")
print("Предсказание: 1 system + 1 пара = 3 элемента. Совпало.")

print("\n=== 2. История после двух обменов (без API) ===")
messages.append(ChatMessage(role="user", content="А как проверить делитель?"))
messages.append(
    ChatMessage(
        role="assistant",
        content="Тестовый ответ без API: сравнить делитель с нулём через if.",
    )
)
show_history(messages, "Два полных обмена")
print("Предсказание: 1 + 2 * 2 = 5 элементов. Совпало.")
print("Обменов 2, а элементов 5, потому что system не относится к обменам.")

print("\n=== 3. Цикл ввода без API ===")
print("Доступные команды: выход, история, очистить.")
print("Любой обычный текст добавляет пару user + тестовый assistant.")
print("Пустая строка пропускается и историю не меняет.")

demo = [ChatMessage(role="system", content=SYSTEM_PROMPT)]

while True:
    raw = input("\nВы: ")
    text = raw.strip()
    command = text.lower()

    if command in ("выход", "exit", "quit"):
        print("Демонстрация завершена.")
        break

    if not text:
        print("Пустой ввод пропущен, история не изменилась.")
        continue

    if command == "очистить":
        demo = [demo[0]]
        print("История очищена: остался только system.")
        show_history(demo, "После очистки")
        continue

    if command == "история":
        show_history(demo, "Текущая история")
        continue

    demo.append(ChatMessage(role="user", content=text))
    demo.append(
        ChatMessage(
            role="assistant",
            content=f"Тестовый ответ без API на: {text}",
        )
    )
    show_history(demo, "После нового обмена")

print("\n=== 4. Ограничение истории (max_pairs = 3) ===")

# Четыре различимые пары: после сокращения должна остаться только одна system
# и три последние пары (2-я, 3-я, 4-я). Первая пара удаляется.
pairs_demo = [ChatMessage(role="system", content=SYSTEM_PROMPT)]
for number in range(1, 5):
    pairs_demo.append(ChatMessage(role="user", content=f"Вопрос {number}"))
    pairs_demo.append(ChatMessage(role="assistant", content=f"Ответ {number}"))

show_history(pairs_demo, "До сокращения (4 пары)")
trimmed = trim_history(pairs_demo)
show_history(trimmed, "После сокращения (не больше 3 пар)")

print("\nПроверка состава после сокращения:")
print(f"  Длина равна 7: {len(trimmed) == 7}")
print(f"  Первый элемент system: {trimmed[0].role == 'system'}")
print(f"  Первая пара удалена: {message_text(trimmed[1]) == 'Вопрос 2'}")
print(f"  Сохранены пары 2, 3, 4: {[message_text(m) for m in trimmed[1:]] == ['Вопрос 2', 'Ответ 2', 'Вопрос 3', 'Ответ 3', 'Вопрос 4', 'Ответ 4']}")
print(f"  Порядок user/assistant не нарушен: {[m.role for m in trimmed[1:]] == ['user', 'assistant'] * 3}")

print("\nИтог: при max_pairs = 3 в истории остаётся не больше 7 сообщений.")
