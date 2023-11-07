def formatapalpite(nletras, listalinhas):
    #condição para titulo de palpites, dependendo do numero de letras
    if nletras == 4:
        visualizapalpites = f"{'-' * 5} > PALPITES < {'-' * 5}\n"
    elif nletras == 5:
        visualizapalpites = f"{'-' * 8} > PALPITES < {'-' * 8}\n"
    elif nletras == 6: 
        visualizapalpites = f"{'-' * 11} > PALPITES < {'-' * 11}\n"
    else: 
        visualizapalpites = f"{'-' * 14} > PALPITES < {'-' * 14}\n"

    # O for percorre a palavra e a transforma em string, formatando ela
    for linha in listalinhas:
                    # o if cria diferentes formatacoes para difererentes numero de letras
                    if nletras == 4:
                        visualizapalpites +=f"{'-' * 25}\n"
                        visualizapalpites +=f"│ {' │ '.join(linha)} │\n"
                        visualizapalpites +=f"{'-' * 25}\n"
                    elif nletras ==5:
                        visualizapalpites +=f"{'-' * 31}\n"
                        visualizapalpites +=f"│ {' │ '.join(linha)} │\n"
                        visualizapalpites +=f"{'-' * 31}\n"
                    elif nletras == 6:
                        visualizapalpites +=f"{'-' * 37}\n"
                        visualizapalpites +=f"│ {' │ '.join(linha)} │\n"
                        visualizapalpites +=f"{'-' * 37}\n"
                    else:
                        visualizapalpites +=f"{'-' * 43}\n"
                        visualizapalpites +=f"│ {' │ '.join(linha)} │\n"
                        visualizapalpites +=f"{'-' * 43}\n"
    return visualizapalpites
