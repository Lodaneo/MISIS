"""
text_stats.py
Script principal do Laboratório 3.
Lê um texto da entrada padrão e exibe:
 - número de palavras únicas
 - as 5 palavras mais frequentes (em formato de tabela)
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import tokenize, count_freq, top_n


def print_table(data: list[tuple[str, int]]):
    """Exibe uma tabela simples e alinhada com as palavras e suas frequências."""
    if not data:
        print("(nenhum dado para mostrar)")
        return

    # Calcula larguras das colunas
    col1_width = max(len(word) for word, _ in data)
    col2_width = max(len(str(count)) for _, count in data)

    # Cabeçalho
    print(f"{'PALAVRA'.ljust(col1_width)} | {'FREQ'.rjust(col2_width)}")
    print("-" * (col1_width + col2_width + 7))

    # Linhas da tabela
    for word, count in data:
        print(f"{word.ljust(col1_width)} | {str(count).rjust(col2_width)}")


if __name__ == "__main__":
    print("=== Analisador de Texto ===")
    text = input("Digite ou cole um texto:\n> ")

    words = tokenize(text)
    freqs = count_freq(words)
    top = top_n(freqs, 5)

    print(f"\nTotal de palavras: {len(words)}")
    print(f"Palavras únicas: {len(freqs)}\n")

    print("Top 5 palavras mais frequentes:")
    print_table(top)
