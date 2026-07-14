numero =  1
soma = 0

while numero <= 500:
    if (numero % 3 == 0) and (numero%2 != 0):
        soma += numero 
    numero += 1
    
print(f"A soma dos números ímpares múltiplos de 3 entre 1 e 500 é: {soma}.")