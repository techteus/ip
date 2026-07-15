nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))

média = (nota1 + nota2) / 2

if média >=9 and média <=10:
    print("Conceito A.")
elif média >= 7.5:
    print("Conceito B.")
elif média >= 6:
    print("Conceito C.")
elif média >= 4:
    print("Conceito D.")
else:
    print("Conceito E.")
