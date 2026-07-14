numero = int(input("Digite um número para descobrir a raiz quadrada: "))

b = 2
p = (b + numero / b) / 2

while abs(p - b) >= 0.0001:
    b = p
    p = (b + numero / b) / 2

print(f"A raiz quadrada de {numero} é aproximadamente {p:.2f}.")
