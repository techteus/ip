votantes = int(input("Digite o número de votantes: "))

monica = 0
cebolinha = 0
magali = 0

for i in range(votantes):
    voto = input(f"Digite o voto {i + 1} (10 para Mônica, 11 para Cebolinha, 12 para Magali): ")

    if voto == "10":
        monica += 1
    elif voto == "11":
        cebolinha += 1
    elif voto == "12":
        magali += 1
    else:
        print("Voto inválido.")

print (f"Mônica recebeu {monica} votos.")
print (f"Cebolinha recebeu {cebolinha} votos.")
print (f"Magali recebeu {magali} votos.")