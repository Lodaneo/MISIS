import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv



caminho_texto="data/lab04/input.txt"
caminho_csv="data/lab04/a.csv"

texto=read_text(caminho_texto)
texto_norma=normalize(texto)
tok=tokenize(texto_norma)
contar=count_freq(tok)
top=top_n(contar)

write_csv(top, caminho_csv, header=("Word", "Count"))
#Write the content in "top" on csv file in path "caminho_csv". Put a header on this
# Header with 2 colunms: "Word", "Count"

print(f"Total of words: {len(tok)}")
print(f"Total of Unique words: {len(contar)}")
print("Top-5:")
for word, count in top:
            print(f"{word}:{count}")