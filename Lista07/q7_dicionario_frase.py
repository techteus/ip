frase = input("Frase -> ")

while frase != "-1":

    dict_frase = {}

    for caractere in frase:
        if caractere in dict_frase:
            dict_frase[caractere] += 1
        else:
            dict_frase[caractere] = 1

    print(f"Dicionário -> {dict_frase}")
    
    frase = input("Frase -> ")
