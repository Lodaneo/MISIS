import re
from collections import Counter

def normalize(text):
    """Remove espaços extras e coloca em minúsculas"""
    text = re.sub(r'\s+', ' ', text.strip())
    return text.lower()

def tokenize(text):
    """Divide o texto em palavras simples"""
    return re.findall(r'\w+', text.lower())

def count_freq(tokens):
    """Conta a frequência das palavras"""
    return dict(Counter(tokens))

def top_n(freq_dict, n=5):
    """Retorna as N palavras mais frequentes"""
    return sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:n]
