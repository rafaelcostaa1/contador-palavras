from collections import Counter
from typing import Dict
import string


def limpar_texto(texto: str) -> str:
    """Remove pontuação e deixa o texto em minúsculo."""
    texto = texto.lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    return texto


def contar_palavras(frase: str) -> Dict[str, int]:
    """Conta a frequência das palavras."""
    frase = limpar_texto(frase)

    if not frase.strip():
        return {}

    return Counter(frase.split())
