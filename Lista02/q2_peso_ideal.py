altura = float(input("Digite sua altura (em metros): "))

peso_ideal_M = (72.7 * altura) - 58
peso_ideal_F = (62.1 * altura) - 44.7

print(f"Seu peso ideal, caso você seja homem é: {peso_ideal_M}kg")
print(f"Seu peso ideal, caso você seja mulher é: {peso_ideal_F}kg")
