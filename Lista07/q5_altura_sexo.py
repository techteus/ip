lista_altura = []
lista_sexo = []

for i in range (10):
    altura = float(input(f"Digite a altura da pessoa {i+1}: "))
    sexo = input(f"Digite o sexo da pessoa {i+1} (M/F): ")

    lista_altura.append(altura)
    lista_sexo.append(sexo)

soma = 0

for i in lista_altura:
    soma += i

media = soma / len(lista_altura)

altura_max = altura_min = media

for i in lista_altura:
    if i < altura_min:
        altura_min = i
    elif i > altura_max:
        altura_max = i

for i in range(len(lista_altura)):
    if lista_altura[i] == altura_min:
        sexo_alturamin = lista_sexo[i]
    elif lista_altura[i] == altura_max:
        sexo_alturamax = lista_sexo[i]

if sexo_alturamax == 'M':
    sexo_alturamax = "masculino"
elif sexo_alturamax == 'F':
    sexo_alturamax = "feminino"

if sexo_alturamin == 'M':
    sexo_alturamin = "masculino"
elif sexo_alturamin == 'F':
    sexo_alturamin = "feminino"

lista_m = []
lista_f = []

for i in range(len(lista_sexo)):
    if lista_sexo[i] == 'M':
        lista_m.append(lista_altura[i])
    elif lista_sexo[i] == 'F':
        lista_f.append(lista_altura[i])

soma_m = 0
soma_f = 0

for i in lista_m:
    soma_m += i

media_m = soma_m / len(lista_m)

for i in lista_f:
    soma_f += i

media_f = soma_f / len(lista_f)

print(f"\nA altura máxima é de uma pessoa do sexo {sexo_alturamax}: {altura_max:.2f}.")
print(f"A altura mínima é de uma pessoa do sexo {sexo_alturamin}: {altura_min:.2f}.")
print(f"A média das alturas masculinas é: {media_m:.2f}.")
print(f"A média das alturas femininas é: {media_f:.2f}.")
print(f"A quantidade de pessoas do sexo masculino é: {len(lista_m)}.")
print(f"A quantidade de pessoas do sexo feminino é: {len(lista_f)}.")