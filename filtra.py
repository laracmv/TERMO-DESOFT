import base_palavras

def filtra(base_palavras, numeroletras):
    # listapalavra -> recebe palavras nº de letras e tamanhos diversos
    listafiltro = []
    for palavra in base_palavras:
        if len(palavra) == numeroletras:
            menor = palavra.lower()
            # menor - formata palavras em minúsculo
            if menor not in listafiltro:
                listafiltro.append(menor)
    return listafiltro