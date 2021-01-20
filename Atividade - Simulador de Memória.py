def bindec(b):
    d = 0
    for i in range(len(b)):
        d += int(b[i]) * (2**((len(b)-1)-i))
    return d

memoria = []

for i in range(16):
    memoria.append("00000000")
    print(memoria[i])
    
while True:
    print("SIMULADOR DE MEMÓRIA\n[W] Escrever\n[R] Ler\n[L] Listar")
    comando = input("Digite uma das opções ou qualquer tecla para parar: ")

    if(comando == "W" or comando == "w"):
        endereco = input("Digite o endereço de 4 bits: ")
        for i in range(len(endereco)):
            if(endereco[i] != "0" and endereco[i] != "1"):
                valido = False
                break
            else: valido = True
        while(len(endereco) != 4 or valido == False):
            print("Endereço inválido!")
            endereco = input("Digite o endereço de 4 bits: ")
            for i in range(len(endereco)):
                if(endereco[i] != "0" and endereco[i] != "1"):
                    valido = False
                    break
                else: valido = True
                
        dado = input("Digite o dado de 8 bits: ")
        for i in range(len(dado)):
            if(dado[i] != "0" and dado[i] != "1"):
                valido = False
                break
            else: valido = True
        while(len(dado) != 8 or valido == False):
            print("Dado inválido!")
            dado = input("Digite o dado de 8 bits: ")
            for i in range(len(dado)):
                if(dado[i] != "0" and dado[i] != "1"):
                    valido = False
                    break
                else: valido = True

        memoria[bindec(endereco)] = dado
        print("Endereço "+endereco+" <--- "+dado)
        print("")

    elif(comando == "R" or comando == "r"):
        endereco = input("Digite o endereço (4 bits) a ser lido: ")
        for i in range(len(endereco)):
            if(endereco[i] != "0" and endereco[i] != "1"):
                valido = False
                break
            else: valido = True
        while(len(endereco) != 4 or valido == False):
            print("Endereço inválido!")
            endereco = input("Digite o endereço (4 bits) a ser lido: ")
            for i in range(len(endereco)):
                if(endereco[i] != "0" and endereco[i] != "1"):
                    valido = False
                    break
                else: valido = True

        print("Endereço: "+endereco+"\nDado: "+memoria[bindec(endereco)])
        print("")
        
    elif(comando == "L" or comando == "l"):
        for i in range(16):
            print(memoria[i])
        print("")
    
    else:
        break
