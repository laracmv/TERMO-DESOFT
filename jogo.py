from inicializa import inicializa
import base_palavras
from filtra import filtra
from posicao_correta import inidica_posicao

print("*"*23)
print("-"*23)
print("- BEM VINDOS AO TERMO! - ")
print("*"*23)
print("-"*23)
print("\nRegras: ")
print("\n - Você tem \033[0;31;40m 6 \033[m tentativas para acertar uma palavra aleatória de 5 letras.")
print(" - A cada tentativa, a palavra testada terá suas letras coloridas conforme:")
print("  ➔ \033[1;49;36m Azul \033[m : A letra está na posição correta;")
print("  ➔ \033[1;49;33m Amarelo \033[m : Tem a letra na palavra mas, não está na posição correta;")
print("  ➔ \033[2;49;39m Cinza \033[m : A letra não existe nesta palavra;")
print("Caso não queria continuar a jogar digite: \033[0;31;40m cansei \033[m")
print('Caso contrário digite: \033[0;31;40m S \033[m para continuar o jogo.\n ')
print("\nBora começar o jogo !!\n")

#definir nossos paramêtros

#5 letras no total
numerodeletras = 5

#delimitar as tentaivas
tentativas = 0

#lista de palavras com 5 letras
listatermos = filtra(base_palavras.PALAVRAS, numerodeletras)

#dicionario com nº de palavras, palavra sorteada, especulacoes e nº de tentativas
dicinicializa = inicializa(listatermos)
print(dicinicializa) #para mostrar a palavra sorteada, só de teste

#o loop de acordo com as regras
#limite de 6 tentativas
while tentativas < 6:
    palpite = input('Digite seu palpite: ')

    #padroniza o palpite em minúsculo
    palpite = palpite.lower()

    #caso cansar do jogo
    if palpite.lower() == "cansei":
        print('Mas já cansou? Até mais então.')
        break

    #se o tamanho do palpite for diferente do numero de letras permitido
    if len(palpite) != numerodeletras: 
        print('Número de letras inválido, a palavra precisa conter 5 letras.')
        continue

    #se palpite for igual a sorteada, ganha o jogo.
    if palpite == dicinicializa["sorteada"]:
        print('\nVocê acertou, parabéns !!\n')
        break

    #posição das letras e cores.
    dicinicializa["especuladas"] += palpite
    listaposicao = inidica_posicao(dicinicializa["sorteada"], palpite)
    print(listaposicao)

    a = ''
    i = 0
    for letra in palpite:
        if listaposicao[i] == 0:
            a+=f"\033[1;49;36m {letra} \033[m"
        elif listaposicao[i] == 1:
            a+=f"\033[1;49;33m {letra} \033[m"
        else: 
            a+=f"\033[2;49;39m {letra} \033[m"
        i+=1
    print(a)

    tentativas +=1

    #se tentativas maior que o esperado, perde o jogo.
    if tentativas >= 6 and palpite != dicinicializa["sorteada"]:
        print(f'Você perdeu, a palavra sorteada era \033[1;49;36m{dicinicializa["sorteada"]}\033[m')

#continuar = input('Deseja continuar o jogo (s/n): ')
#if continuar == 's':













