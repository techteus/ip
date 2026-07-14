renda_hora = float(input("Digite quantos reais você ganha por hora: "))
horas_trabalhadas = float(input("Digite quantas horas você trabalha por mês: "))

salario = renda_hora * horas_trabalhadas
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liquido = salario - (ir + inss + sindicato)

print(f"Salário bruto: R${salario}")
print(f"IR (11%): R${ir}")
print(f"INSS (8%): R${inss}")
print(f"Sindicato (5%): R${sindicato}")
print(f"Salário líquido: R${salario_liquido}")