def inidica_posicao(sorteada, especulada):
    if len(sorteada) != len(especulada):
        vazio = [] #lista vazia pra tamanho diferente
        return vazio

    termo = []
    for palavra in range(len(sorteada)):
        l_sort = sorteada[palavra]
        l_espe = especulada[palavra]

        if l_sort == l_espe:
            termo.append(0) #tá na position certa
        elif l_espe in sorteada:
            termo.append(1) #tem a letra na word
        else:
            termo.append(2) #não tem na word

    return termo
