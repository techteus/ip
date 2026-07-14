deposito = float(input("Digite o valor do depósito inicial: "))
juros = float(input("Digite a taxa de juros (em %): ")) / 100

for mes in range(1, 25):
    deposito += deposito * juros 
    print(f"Mês {mes}: R$ {deposito:.2f}")