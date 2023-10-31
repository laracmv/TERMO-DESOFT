def filtra(listapalavra, numeroletras):
    listafiltro = []
    for palavra in listapalavra:
        if len(palavra) == numeroletras:
            menor = palavra.lower()
            if menor not in listafiltro:
                listafiltro.append(menor)
    return listafiltro