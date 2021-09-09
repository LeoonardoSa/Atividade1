import random

print("Você está na sala: 1")

sala = 1
iteracoes = 0


while iteracoes < 7 and sala < 6:

    print("Escolha seu caminho: ")
    print("[1] - Caminho vermelho")
    print("[2] - Caminho preto")
    caminho = int(input())

    if(caminho == 1):
        sala +=1
        iteracoes += 1
        print("Você está na sala: ", sala)


    elif(caminho == 2):
        iteracoes += 1
        sala +=2    
        print("Você está na sala: ", sala)

if sala == 6:

    while iteracoes < 7 and sala < 8:
        
        print("Escolha seu caminho: ")
        print("[2] - Caminho preto")
        caminho = int(input())

        if(caminho == 2):
            iteracoes += 1
            sala +=2    
            print("Você está na sala: ", sala)


        elif(caminho != 2):
            print("Só exite um caminho!")

while (iteracoes < 7 and sala < 9) and sala != 6:  
    
    print("Escolha seu caminho: ")
    print("[1] - Caminho vermelho")
    print("[2] - Caminho preto")
    caminho = int(input())

    if(caminho == 1):
        iteracoes += 1
        sala +=1    
        print("Você está na sala: ", sala)


    elif(caminho == 2 and sala == 8):
        sala = random.randint(1,5)
        iteracoes += 1
        print("Você está na sala: ", sala)

    else:
        iteracoes += 1
        sala +=2    
        print("Você está na sala: ", sala)

while iteracoes < 7 and sala < 8:
    
    print("Escolha seu caminho: ")
    print("[2] - Caminho preto")
    caminho = int(input())

    if(caminho == 2):
        iteracoes += 1
        sala +=2    
        print("Você está na sala: ", sala)


    elif(caminho != 2):
        print("Só exite um caminho!")  
            

while (iteracoes < 7 and sala < 9) and sala != 6:  
    
    print("Escolha seu caminho: ")
    print("[1] - Caminho vermelho")
    print("[2] - Caminho preto")
    caminho = int(input())

    if(caminho == 1):
        iteracoes += 1
        sala +=1    
        print("Você está na sala: ", sala)


    elif(caminho == 2 and sala == 8):
        sala = random.randint(1,5)
        iteracoes += 1
        print("Você está na sala: ", sala)

    else:
        iteracoes += 1
        sala +=2    
        print("Você está na sala: ", sala) 


if iteracoes > 6 :
    print("Ultrapassou o Número de Jogadas Permitidas")
elif sala == 9:
    print("Parabéns Vocês Venceram Essa Dungeon")