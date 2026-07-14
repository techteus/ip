codigo = int(input("Digite o código do produto: "))

preco = 0
total_compras = 0

while codigo != 0:
    quantidade = int(input("Digite a quantidade do produto: "))

    if codigo == 1:
        preco = 5.50
    elif codigo == 2:
        preco = 2.30
    elif codigo == 3:
        preco = 4.75
    elif codigo == 4:
        preco = 6.80
    elif codigo == 5:
        preco = 9.30
    else:
        print("Código inválido.")
        codigo = int(input("Digite o código do produto: "))
        continue

    total = quantidade * preco
    total_compras += total
    print(f"O total das compras é: R${total_compras:.2f}.")

    codigo = int(input("Digite o código do produto (0 para sair): "))




