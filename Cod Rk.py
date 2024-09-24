import os

# Limpa o terminal.
os.system("cls || clear")


##Turma - G93313

#Nome completo dos componentes.
#1 - Gabriel Pinto dos Santos
#2 - Henrique Santos Silva


print("""
escreva o código do prato para fazer o pedido:
codigo |Menu              |Valor |
1      |Picanha           |100,00|
2      |Strognoff         |35,00 |
3      |Lasanha           |25,00 |
4      |Frango a Milanesa |70,00 |
5      |Peixe Grelhado    |60,00 |  
6      |Burrito com Fritas|85,00 |
7      |Hamburguer        |25,00 |  
""")

def exibir_menu(codigo_prato):
    match(codigo_prato):
        case 1:
            return "Picanha 1", 100.00
        case 2:
            return "Strognoff 2", 35.00
        case 3:
            return "Lasanha 3", 25.00
        case 4:
            return "Frango a Milanesa 4", 70.00
        case 5:
            return "Peixe Grelhado 5", 60.00
        case 6:
            return "Burrito com Fritas 6", 85.00
        case 7:
            return "Hamburguer 7", 25.00
        case _:
            return None, 0

pedido_cliente = []
total_do_pedido = 0

while True:
    codigo_prato = int(input("Digite o codigo do produto: "))
    prato, preco = exibir_menu(codigo_prato)
    if prato is None:
        print("Codigo invalido,Digite o codigo novamente: ")
    else:
        print(f"Prato escolhido: {prato} R$ {preco:.2f}")
        pedido_cliente.append((prato, preco))  # Armazena o prato e o preço
        total_do_pedido += preco

        adicionar = input("Deseja adicionar mais algum pedido? (sim ou não): ")
        if adicionar.lower() != 'sim':
            break

def calcular_valor_final(total):
    forma_pagamento = input("Escolha a forma de pagamento (1 - À vista / 2 - Cartão de crédito): ")
    if forma_pagamento == '1':
        desconto = total * 0.10
        total_final = total - desconto
        tipo_pagamento = "À vista"
    elif forma_pagamento == '2':
        acrescimo = total * 0.10
        total_final = total + acrescimo
        tipo_pagamento = "Cartão de crédito"
    else:
        print("Forma de pagamento inválida.")
        desconto = total * 0.10
        total_final = total - desconto
        tipo_pagamento = "À vista"

    return tipo_pagamento, desconto if 'desconto' in locals() else acrescimo, total_final

tipo_pagamento, ajuste, total_final = calcular_valor_final(total_do_pedido)

print("\n=== Pedidos realizados ===")
for item, preco in pedido_cliente:
    print(f"- {item}: R$ {preco:.2f}")
print(f"Total a pagar : R$ {total_final:.2f} (Valor sem adição de desconto ou acrecimo: {total_do_pedido}) ({tipo_pagamento})")
print("=== FIM ===")
