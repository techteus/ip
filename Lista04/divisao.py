numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

numero1_backup = numero1

divisao = 0

while numero1 >= numero2:
    numero1 -= numero2
    divisao += 1

print(f"A divisão inteira de {numero1_backup} por {numero2} é: {divisao}.")
print(f"O resto da divisão é: {numero1}.")