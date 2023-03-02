print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

#valores = ['gabirle', 'jonata']

#for nome in valores:
 #   print(nome)

for rodada in range(1,total_de_tentativas + 1):
    #print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    print(f"Tentativa {rodada} de {total_de_tentativas}")

    chute_str = input("Digite um numero de 1 a 100: ")
    print("Você digitou " , chute_str)
    chute = int(chute_str)
    
    if(chute < 1 or chute > 100):
        print("Digite apenas números de 1 a 100!!!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Parabéns! Você acertou!")
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")


print("Fim do jogo")