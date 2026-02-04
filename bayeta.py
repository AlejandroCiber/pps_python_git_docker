import random

frases = [
    "Hoy será un gran día",
    "La fortuna te sonríe",
    "Sorpresas agradables están por venir",
    "Confía en tu intuición",
    "Una nueva oportunidad se acerca"
]

def frotar(n_frases: int = 1) -> list:
    return random.choices(frases, k=n_frases)

