from random import randint

lancamento = int(input("Digite quantas vezes o dado será lançado: "))

lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []

for i in range(lancamento):
    dado = randint(1,6)
    if dado == 1:
        lista1.append(dado)
    elif dado == 2:
        lista2.append(dado)
    elif dado == 3:
        lista3.append(dado)
    elif dado == 4:
        lista4.append(dado)
    elif dado == 5:
        lista5.append(dado)
    else:
        lista6.append(dado)

porcentagem1 = (len(lista1)/lancamento)*100
porcentagem2 = (len(lista2)/lancamento)*100
porcentagem3 = (len(lista3)/lancamento)*100
porcentagem4 = (len(lista4)/lancamento)*100
porcentagem5 = (len(lista5)/lancamento)*100
porcentagem6 = (len(lista6)/lancamento)*100

print(f"Porcentagem de vezes que o número 1 apareceu: {porcentagem1:.2f}%")
print(f"Porcentagem de vezes que o número 2 apareceu: {porcentagem2:.2f}%")
print(f"Porcentagem de vezes que o número 3 apareceu: {porcentagem3:.2f}%")
print(f"Porcentagem de vezes que o número 4 apareceu: {porcentagem4:.2f}%")
print(f"Porcentagem de vezes que o número 5 apareceu: {porcentagem5:.2f}%")
print(f"Porcentagem de vezes que o número 6 apareceu: {porcentagem6:.2f}%")


