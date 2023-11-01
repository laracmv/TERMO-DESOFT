from inicializa import inicializa
import base_palavras
from filtra import filtra
from posicao_correta import inidica_posicao

print("*"*23)
print("-"*23)
print("- BEM VIADOS AO TERMO! - ")
print("*"*23)
print("-"*23)
print("\nCansou? digite: cansei")
print("\nRegras: ")
print("\n - Você tem \033[0;31;40m n \033[m tentivas para acertas uma palavra aleatória de 5 letras.")
print(" - A cada tentativa, a palavra testada terá suas letras coloridas conforme:")
print("  ➔ \033[1;49;36m Azul \033[m : a letra está na posição correta;")
print("  ➔ \033[1;49;33m Amarelo \033[m : a letra está na posição correta;")
print("  ➔ \033[2;49;39m Cinza \033[m : a letra está na posição correta;")

numerodeletras = int(input("\nDiga quantas letras você quer, entre 4 e 7: "))
palpite = " "
# listatermos -> cria uma lista de palavras com mesmo numero de letras
listatermos = filtra(base_palavras.PALAVRAS, numerodeletras)

#dicinicializa -> cria um dicionario com nº de palavras, palavra sorteada, especulacoes e nº de tentativas
dicinicializa = inicializa(listatermos)
print(dicinicializa)

while palpite not in dicinicializa["sorteada"]:
    palpite = input('Digite seu palpite: ')
    # palpite.lower -> padroniza o palpite em minúsculo
    palpite = palpite.lower()
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













