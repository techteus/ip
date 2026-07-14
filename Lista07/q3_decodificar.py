dict_codigo = {0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}

codigo = int(input("Digite o código a ser decodificado (-1 para sair): "))

lista_codigo = []

while codigo != -1:
    lista_codigo.append(codigo)
    codigo = int(input("Digite o código a ser decodificado (-1 para sair): "))

mensagem = ""

for i in lista_codigo:
    mensagem += dict_codigo[i]


print(mensagem)