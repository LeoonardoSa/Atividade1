
print("Você está na sala: 1")

sala = 1



while sala < 9:
    print("Escolha seu caminho: ")
    print("[1] - Caminho vermelho")
    print("[2] - Caminho preto")
    caminho = int(input())

    if(sala == 6):
        
        print("Escolha seu caminho: ")
        print("[2] - Caminho preto")
        caminho = int(input())
        sala =+ 2

    elif(sala == 8):
        print("Escolha seu caminho: ")
        print("[1] - Caminho vermelho")
        print("[2] - Caminho preto")
        caminho = int(input())


print("PARABENS NERDOLA")
