
divida = float(input("Digite o valor da dívida: "))
juros = float(input("Digite a taxa de juros mensal (em %): ")) / 100
valor_pago = float(input("Digite o valor pago mensalmente: "))

meses = 0
juros_total = 0
total_pago = 0

while divida > 0:
    meses += 1  
    juros_total += (divida * juros)
    divida += divida * (juros)  

    if valor_pago > divida:
        valor_pago = divida
        
    divida -= valor_pago 
    total_pago += valor_pago

print(f"Serão necessários {meses} meses para quitar a dívida.")
print(f"O valor total pago será de R${total_pago:.2f}.")
print(f"O valor total de juros pago será de R${juros_total:.2f}.")

