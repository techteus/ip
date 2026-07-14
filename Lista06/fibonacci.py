numero = int(input("Insira quantos numeros você deseja ver da sequência de Fibonacci: "))

anterior1 = 0
anterior2 = 1

for i in range(numero):
    if i == 1:
        print(1)
    else:
        fibonacci = anterior1 + anterior2
        print(fibonacci)
        anterior1 = anterior2
        anterior2 = fibonacci