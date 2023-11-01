import random

def inicializa(listadepalavras):
    # listadepalavras -> recebe palavras com mesmo tamanho
    dinicializado = {}
    # dinicializado -> dicionario c conf do jogo
    dinicializado["n"] = len(listadepalavras[0])
    # n -> número de letras
    dinicializado["sorteada"] = random.choice(listadepalavras)
    dinicializado["especuladas"] = []
    dinicializado["tentativas"] = dinicializado["n"] + 1
    # tentativas -> n + 1
    return dinicializado