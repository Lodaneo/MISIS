import sys
import os
# Permite importar o módulo lib.text de uma pasta acima (sem mudar nada no projeto)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib import text  # usa o mesmo módulo já usado em text_status.py

print("=== Testes das funções do text.py ===\n")

print(text.normalize("  двойные   пробелы  "))
print(text.tokenize("Привет, мир! Привет!!!"))

tokens = ["a", "b", "a", "c", "b", "b"]
freq = text.count_freq(tokens)
print(freq)
print(text.top_n(freq))
