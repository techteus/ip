numero = int(input("Insira um número para verificar se é primo: "))
divisores = 0

if numero == 0 or numero == 1:
    print(f"{numero} não é primo.")

else:
    if numero == 2:
        print(f"{numero} é primo.")
    else:
        for i in range(2, numero):
            if numero % i == 0:
                divisores +=1
    
        if divisores == 0:
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo.")
