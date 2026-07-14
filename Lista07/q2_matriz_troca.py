matriz = []

for i in range (3):
    linha = []
    for j in range(3):
        elemento = int(input(f"Digite o valor do elemento [{i}][{j}]: "))
        linha.append(elemento)
    matriz.append(linha)

linha2 = []
coluna2 = []

for i in range (3):
    for j in range(3):
        if i == 2:
            linha2.append(matriz[i][j])
        if j == 2:
            coluna2.append(matriz[i][j])

for i in range(3):
    for j in range(3):
        if i == 2:
            matriz[i][j] = coluna2[j]
        if j == 2:
            matriz[i][j] = linha2[i]

print(matriz[0])
print(matriz[1])
print(matriz[2])