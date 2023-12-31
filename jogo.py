from inicializa import inicializa
import base_palavras
from filtra import filtra
from posicao_correta import inidica_posicao
from formatacaopalpites import formatapalpite

print("*"*23)
print("-"*23)
print("- BEM VINDOS AO TERMO! - ")
print("*"*23)
print("-"*23)
print("\nRegras: ")
print("\n - Você pode escolher entre 4, 5, 6 ou 7 letras para acertar uma palavra aleatória!")
print(" - Você tem o número de letras + 1 de tentativas para acertar!")
print(" - A cada tentativa, a palavra testada terá suas letras coloridas conforme:")
print("   ➔ \033[1;49;36m Azul \033[m : A letra está na posição correta;")
print("   ➔ \033[1;49;33m Amarelo \033[m : Tem a letra na palavra mas, não está na posição correta;")
print("   ➔ \033[2;49;39m Cinza \033[m : A letra não existe nesta palavra;")
print(" - Os acentos são ignorados.")
print(" - As palavras podem possuir letras repetidas.")
print('A cada palavra acertada, você pontua de acordo com o n° de letras:')
print('   ➔ 4 letras valem  \033[1;49;33m10 pontos. \033[m ')
print('   ➔ 5 letras valem  \033[1;49;33m20 pontos. \033[m ')
print('   ➔ 6 letras valem  \033[1;49;33m30 pontos. \033[m ')
print('   ➔ 7 letras valem  \033[1;49;33m40 pontos. \033[m ')
print("Caso não queria continuar a jogar digite: \033[1;49;31m cansei \033[m")
print("\nBora começar o jogo !!\n")



jogardenovo = ""
pontos = 0
#Loop para escolher se que ou não jogar de nv
while jogardenovo != "N" and jogardenovo != "n":

    #5 letras no total
    numerodeletras = int(input(("\nDigite quantas letras você quer jogar, pode ser 4, 5, 6 ou 7: ")))
    print('\n')
    
    #excessão caso o usuario digite o valor errado
    opcoesnumerodeletras = [4,5,6,7]
    if numerodeletras not in opcoesnumerodeletras:
        while numerodeletras not in opcoesnumerodeletras:
            print("Valor incorreto, digite novamente")
            numerodeletras = int(input(("\nDigite quantas letras você quer jogar, pode ser 4, 5, 6 ou 7: ")))
            
    #lista de palavras com 5 letras
    listatermos = filtra(base_palavras.PALAVRAS, numerodeletras)

    #dicionario com nº de palavras, palavra sorteada, especulacoes e nº de tentativas
    dicinicializa = inicializa(listatermos)
    

    #delimitar as tentativas
    tentativas = dicinicializa["tentativas"]

    palpite = ""
    f = 0
    # Numero tentativas -> numero de vezes que o jogador tentou
    numero_tentativas = 0
    
    #listadepalpites -> usado na formatação dos palpites
    listadepalpites = []
    while (tentativas > 0 and tentativas <= dicinicializa["tentativas"]) and  (palpite != dicinicializa["sorteada"]) and (palpite != "cansei") and (palpite != "cansei mesmo"):
        palpite = input('Digite seu palpite: ')
        print('\n')

        #padroniza o palpite em minúsculo
        palpite = palpite.lower()
       
        #caso cansar do jogo
        if palpite == "cansei":
            palpite = input("Não seja um mal perdedor, você tem certeza? [cansei mesmo/ N]: ")
            if palpite == "cansei mesmo":
                print('\n>>> Então tá bom, volte sempre.')

        elif palpite in dicinicializa["especuladas"]:
            print("Essa palavra já foi dita, diga outra! ")
        
        #se o tamanho do palpite for diferente do numero de letras permitido
        elif len(palpite) != numerodeletras: 
            print(f"\nNúmero de letras inválido, a palavra precisa conter {dicinicializa['n']} letras.")
        
        elif palpite not in base_palavras.PALAVRAS:
            print("Palavra desconhecida, tente outra\n")

        else:
            numero_tentativas += 1
            #se palpite for igual a sorteada, aumenta a pontuação de acordo com o n° de letras.
            if palpite == dicinicializa["sorteada"] and numerodeletras == 4:
                base = 10
                pontos += base
                print(f"\n>>> Você acertou depois de {numero_tentativas} tentativa, parabéns !!!\nVocê possui \033[1;49;33m{pontos}\033[m pontos.\n")
            elif palpite == dicinicializa["sorteada"] and numerodeletras == 5:
                base = 20
                pontos += base
                print(f"\n>>> Você acertou depois de {numero_tentativas} tentativa, parabéns !!!\nVocê possui \033[1;49;33m{pontos}\033[m pontos.\n")
            elif palpite == dicinicializa["sorteada"] and numerodeletras == 6:
                base = 30
                pontos+= base
                print(f"\n>>> Você acertou depois de {numero_tentativas} tentativa, parabéns !!!\nVocê possui \033[1;49;33m{pontos}\033[m pontos.\n")
            elif palpite == dicinicializa["sorteada"] and numerodeletras == 7:
                base = 40
                pontos += base
                print(f"\n>>> Você acertou depois de {numero_tentativas} tentativa, parabéns !!!\nVocê possui \033[1;49;33m{pontos}\033[m pontos.\n")
            else: 
                #adiciona os palpites a uma lista dentro de dicinicializa["especuladas"]
                dicinicializa["especuladas"].append(palpite)
                listaposicao = inidica_posicao(dicinicializa["sorteada"], palpite)

                i = 0
                linhaatual = []
                for letra in palpite:
                    if listaposicao[i] == 0:
                        linhaatual.append(f"\033[1;49;36m {letra} \033[m")
                    elif listaposicao[i] == 1:
                        linhaatual.append(f"\033[1;49;33m {letra} \033[m")
                    else: 
                        linhaatual.append(f"\033[2;49;39m {letra} \033[m")
                    i+=1

                #possibilita que os palpites anteriores aparecam para o usuario
                listadepalpites.append(linhaatual)
                print(formatapalpite(numerodeletras, listadepalpites))

                # Diminui o numero de tentativas ate chegar em 0
                f+=1
                tentativas = dicinicializa["tentativas"] - f
                if tentativas == 0:
                    print(f'\n>>> Você perdeu, a palavra sorteada era: \033[1;49;36m{dicinicializa["sorteada"]}\033[m\n')
                else: 
                    print(f'\nFaltam {tentativas} tentativas\n')
    
    jogardenovo = input("Gostaria de jogar de novo? [S/N]: ")
    if jogardenovo == 'n' and 'N':
        print(f'\nSua pontuação total foi de \033[1;49;33m{pontos}\033[m pontos.\n')
      
print("Até a próxima rodada!\n")














