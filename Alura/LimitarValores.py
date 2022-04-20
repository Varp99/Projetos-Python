print("*******************")
print("Jogo de adivinhação")
print("*******************")

#Definição do número a ser adivinhado
numero_secreto = 42
#Definição da quantidade de tentativas
tentativas = 3

#Faz rodar o código 3x
for rodada in range(1,tentativas + 1):
    #Acompanhar em qual tentativa está / print("Tentativa",rodada,"de",tentativas)
    #Melhor maneira, o format pega os dados e coloca dentro dos colchetes
    print("Tentativa {} de {}".format(rodada, tentativas))
    #Pedir para a pessoa digitar um número
    chute_str = input("Digite o seu número:")
    print("Você digitou", chute_str)

    #Limita os Valores
    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100 !")
        #Continua a próxima interação do for lá em cima
        continue

    #Transformar a string em int
    chute = int(chute_str)
    #Variaveis de condição
    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    #Condições para verificar se o número foi adivinhado ou não
    if(acertou):
        print("Você acertou")
        #Para parar o código quando acertar, no caso ele sai do laço
        break
    else:
        if(chute_maior):
            print("Você errou! O chute foi maior do que o número secreto!")
            print("Continue")
        elif(chute_menor):
            print("Você errou! O chute foi menor do que o número secreto!")
            print("Continue")

print("Fim do Jogo")