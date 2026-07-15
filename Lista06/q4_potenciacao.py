base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
potencia = 1

for i in range(expoente):
    potencia *= base

print(f"Base {base} elevada ao expoente {expoente} é igual a {potencia}.")
