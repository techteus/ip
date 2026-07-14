
quant_pontos = int(input("Digite a quantidade de pontos: "))

lista_pontos = []
for i in range(quant_pontos):
    x = int(input(f"Digite a coordenada x do ponto {i+1}: "))
    y = int(input(f"Digite a coordenada y do ponto {i+1}: "))
    ponto = (x, y)
    lista_pontos.append(ponto)

# distancia minima media e maxima entre os pontos:
distancias = []
for i in range(len(lista_pontos)):
    for j in range(i + 1, len(lista_pontos)):
        ponto1 = lista_pontos[i]
        ponto2 = lista_pontos[j]
        distancia = ((ponto2[0] - ponto1[0]) ** 2 + (ponto2[1] - ponto1[1]) ** 2) ** 0.5
        distancias.append(distancia)

soma = 0

for i in distancias:
    soma +=i

distancia_media = soma / len(distancias)

distancia_minima = distancia_maxima = distancia_media

for distancia in distancias:
    if distancia < distancia_minima:
        distancia_minima = distancia
    elif distancia > distancia_maxima:
        distancia_maxima = distancia

print(f"\nA distância mínima entre os pontos é: {distancia_minima:.2f}.")
print(f"A distância máxima entre os pontos é: {distancia_maxima:.2f}.")
print(f"A distância média entre os pontos é: {distancia_media:.2f}.")