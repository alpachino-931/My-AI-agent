# Задание 24. Ошибка в словаре
import os
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

document = {
    "source": "python_basics.txt",
    "text": "Python — язык программирования."
}

print(document)
