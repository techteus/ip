lista1 = []
lista2 = []

for i in range(5):
    elemento = int(input("Digite o valor do elemento (Vetor 1): "))
    lista1.append(elemento)
for i in range(5):
    elemento = int(input("Digite o valor do elemento (Vetor 2): "))
    lista2.append(elemento)

print(lista1,lista2)

lista3 = []

for i in range(5):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)