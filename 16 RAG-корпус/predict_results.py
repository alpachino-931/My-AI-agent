# Уровень 9. Предскажи результат
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "  Python  "
print(text.strip())

lines = ["A", "", "B"]
print(len(lines))

documents = [{"source": "a.txt", "text": "ABC"}]
print(documents[0]["source"])
