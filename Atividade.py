
print("Você está na sala: 1")

sala = 1



while sala < 9:
    print("Escolha seu caminho: ")
    print("[1] - Caminho vermelho")
    print("[2] - Caminho preto")
    caminho = int(input())

    if(caminho == 1):
        sala +=1
        print("Você está na sala: ", sala)


    elif(caminho == 2):
        sala +=2    
        print("Você está na sala: ", sala)


print("PARABENS NERDOLA")
