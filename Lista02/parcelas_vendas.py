valor = float(input("Digite o valor do produto comprado: "))
pagamento = input("Digite a forma de pagamento (Dinheiro, Cheque ou Cartão): ")

if pagamento == "Dinheiro" or pagamento == "Cheque":
    if pagamento == "Dinheiro" and valor >= 100:
        valor_desconto = valor * 0.9
        print(f"R${valor_desconto}")
    else:
        print(f"R${valor}")

elif pagamento == "Cartão":
    funçao = input("Digite a função do cartão (Débito ou Crédito): ")
    if funçao == "Crédito":
        parcelas = int(input("Digite o número de parcelas (1, 2 ou 3): "))
        if parcelas == 1 or parcelas == 2 or parcelas == 3:
            valor_parcela = valor / parcelas
            print(f"R${valor}")
            print(f"{parcelas} parcelas de R${valor_parcela}")
        else:
            print("Quantidade de parcelas inválida.")
    elif funçao == "Débito":
        print(f"R${valor}")
    else:
        print("Forma de pagamento inválida.")

else:
    print("Forma de pagamento inválida.")
