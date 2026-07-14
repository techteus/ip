valor = float(input("Digite o valor do produto comprado: "))
pagamento = input("Digite a forma de pagamento (Dinheiro ou Cheque): ")

if pagamento == "Dinheiro" or pagamento == "Cheque":
    if pagamento == "Dinheiro" and valor >= 100:
        valor_desconto = valor * 0.9
        print(f"R${valor_desconto}")
    else:
        print(f"R${valor}")
else:
    print("Forma de pagamento inválida.")