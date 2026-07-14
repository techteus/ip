numero = int(input("Digite um número (-1 para sair): "))

menor = maior = numero
soma = 0

while numero != -1:
    if numero < menor:
        menor = numero
    elif numero > maior:
        maior = numero
    soma += numero
    numero = int(input("Digite um número (-1 para sair): "))

print(f"O maior valor digitado foi: {maior}")
print(f"O menor valor digitado foi: {menor}")
print(f"A soma dos valores digitados foi: {soma}")
