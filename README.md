# Мой ИИ-агент (My-AI-agent)

Практические работы по курсу «Искусственный интеллект».
Автор: Лучаев Ефим Романович, группа 1ИИ-1-11.

Каждый день — в отдельной папке: код помощника, отчёт, журнал экспериментов
(`experiment_dayNN.txt`), тесты/проверки (`tests_dayNN.txt`) и последние запуски
(`last_prompt.txt`, `last_answer.txt`, `history_result.txt`, `chat_history.txt`).

## Структура

| Папка | Тема | Статус |
|---|---|---|
| `13 Промпт-шаблоны` | Промпт-шаблоны и настройки своего ИИ-помощника | готово |
| `14 История` | Диалог с историей | готово |
| `15 Ошибки и Pydantic` | Ошибки API, логирование и структурированный вывод | готово |
| `16 RAG-корпус` | RAG: подготовка корпуса документов | код готов |
| `17 Нормализация` | RAG: очистка и нормализация корпуса | готово |
| `18 Чанки` | RAG: разбиение документов на чанки | готово |

Внутри `13 Промпт-шаблоны`:

- `main.py` — итоговая версия помощника (поиск и исправление ошибок в коде).
- `main_before_day13.py` — версия до доработки, для сравнения.
- `prompts.py` — системная инструкция (роль, структура ответа, ограничения).
- `certs/` — корневой сертификат для доступа к GigaChat.
- `experiment_day13.txt`, `tests_day13.txt` — журнал экспериментов и результаты тестов.
- `last_prompt.txt`, `last_answer.txt` — последний отправленный запрос и ответ модели.

Внутри `14 История`:

- `main.py` — чат с историей: команды `выход`, `очистить`, `история`, лимит `max_pairs`.
- `main_before_day14.py` — рабочая версия 13 дня до переделки.
- `prompts.py` — та же системная инструкция, что и на 13 дне.
- `history_demo.py` — проверка истории, цикла и сокращения без API.
- `history_result.txt` — вывод демонстрации без API.
- `chat_history.txt` — текстовый журнал реального диалога.
- `report_day14.txt` — план, предсказания, проверки и пример диалога.
- `certs/` — сертификат для доступа к GigaChat.

Внутри `15 Ошибки и Pydantic`:

- `api_errors.py` — try / except, объект ошибки и коды ответов API.
- `logging_demo.py` — настройка `logging`, уровни INFO / WARNING / ERROR.
- `structured_output.py` — модели Pydantic, `Field`, `chat_parse(strict=True)`.
- `final_day15.py` — итоговый анализатор ошибок в коде.
- `task27_question_analyzer.py`, `task28_student_extractor.py`,
  `task29_request_classifier.py` — мини-программы заданий 27–29.
- `app.log` — журнал событий без ключа API.
- `result.txt` — структурированный результат последнего запуска.
- `report_day15.txt` — примеры, код заданий, контрольные вопросы.
- `certs/` — сертификат для доступа к GigaChat.

Внутри `16 RAG-корпус`:

- `corpus/`, `corpus_git/` — тематические TXT-корпуса.
- `cleaned/` — очищенные копии документов.
- `final_day16.py` — итоговая подготовка корпуса.
- `task01_…` … `task28_…` — задания по уровням.
- `star1_category.py`, `star2_average_length.py`, `star3_summary_csv.py` — звёздочки.
- `corpus_summary.csv` — сводка корпуса.

Внутри `17 Нормализация`:

- `text_normalization.py` — `clean_line()`, `normalize_text()`, удаление дублей.
- `normalize_corpus.py` — нормализация всех файлов из `cleaned/` в `normalized/`.
- `final_day17.py` — итоговая программа с CSV-отчётом и проверкой пустых файлов.
- `tasks_01_08_spaces_and_lines.py` … `tasks_29_30_projects.py` — задания по уровням.
- `star1_…`, `star2_…`, `star3_…` — задания со звёздочкой.
- `cleaned/`, `normalized/` — корпус до и после нормализации.
- `dirty_instruction.txt`, `cleaned_instruction.txt` — демонстрация очистки.
- `corpus_report.csv` — размеры до/после и процент сокращения.
- `console_day17.txt` — вывод всех запусков.
- `report_day17.txt` — отчёт с проверками и контрольными вопросами.

Внутри `18 Чанки`:

- `chunking.py` — `split_into_chunks()`, `split_with_overlap()` с проверкой параметров.
- `chunk_corpus.py` — полный пример чанкинга корпуса из методички.
- `final_day18.py` — итоговая программа: `300/50`, `chunks/`, `chunks_summary.csv`.
- `tasks_01_08_simple_overlap.py` … `tasks_30_31_projects.py` — задания по уровням.
- `star1_two_parameter_sets.py` — сравнение `200/40` и `400/80`.
- `star2_document_index.py` — поле `document_index`, `chunks_with_index.csv`.
- `star3_jsonl.py` — все чанки в `chunks.jsonl`.
- `normalized/` — корпус Дня 17, `chunks/` — 13 готовых чанков.
- `chunks_summary.csv` — `source`, `chunk_id`, `length`.
- `console_day18.txt` — вывод всех запусков.
- `report_day18.txt` — отчёт с проверками и контрольными вопросами.

День 19 (эмбеддинги) будет добавлен по мере выполнения.

## Запуск

1. Python 3.13+ и пакеты: `pip install gigachat python-dotenv`
2. В корне проекта — файл `.env` с ключами `GIGACHAT_CREDENTIALS` и `GIGACHAT_SCOPE`.
3. Перейти в папку нужного дня и запустить: `python main.py`

## Важно

`.env`, `.venv/` и методички (`*.docx`) в репозиторий не выгружаются.
Сертификат `certs/` лежит в каждой папке дня — папка запускается автономно.
