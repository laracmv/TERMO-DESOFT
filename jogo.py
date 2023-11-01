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
especuladas = []
palavra = input('Digite a palavra especulada: ')
especuladas.append(palavra)

# listatermos -> cria uma lista com o número de letras do mesmo tamanho das palavras
listatermos = filtra(base_palavras.PALAVRAS, numerodeletras)

dicinicializa = inicializa(listatermos)
if dicinicializa["sorteada"] not in dicinicializa["especuladas"]:

#essa lista serve pra apendar os valores, se ta certo, errado, ou tem na word
listaposicao = inidica_posicao(dicinicializa["sorteada"], dicinicializa["especuladas"])












