"""
Informe o número da turma: 
Turma - G93313

Nome completo dos componentes.
1 - Gabriel Pinto dos Santos
2 - Henrique Santos Silva
"""


import os

# Limpa o terminal.
os.system("cls || clear") 

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
                return "Picanha R$ 100,00",100
            case 2:
                return "Strognoff R$ 35,00",35
            case 3:
                return "Lasanha R$ 35,00",35
            case 4:
                return "Frango a Milanesa R$ 70,00",70
            case 5:
                return "Peixe Grelhado R$ 60,00",60
            case 6:
                return "Burrito com Fritas R$ 85,00",85
            case 7:
                return "Hamburguer R$25,00",25
            case _:
                return None, 0

Pedido_client = []
total_do_pedido = 0


while True:
    codigo_prato = int(input("Digite o codigo do produto: "))
    prato, preco = exibir_menu(codigo_prato)
    if prato is None:
        print("Codigo invalido,Digite o codigo novamente: ")
    else:
        print(f"Prato ecolhido: {prato}")
        Pedido_client.append(prato)
        total_do_pedido += preco
    
        adicionar = input("Deseja Adiciconar mais algum pedido? (sim ou não ?):")
        if adicionar != 'sim':
            break

    def calcular_valor_final(total):

        forma_pagamento = input("Escolha a forma de pagamento (1 - À vista / 2 - Cartão de crédito): ")
        if forma_pagamento == '1':
            desconto = total * 0.10
            total_final = total - desconto
            tipo_pagamento = "À vista"
        elif forma_pagamento == '2':
            acréscimo = total * 0.10
            total_final = total + acréscimo
            tipo_pagamento = "Cartão de crédito"
        else:
            print("Forma de pagamento inválida. Considerando 'À vista' por padrão.")
        desconto = total * 0.10
        total_final = total - desconto
        tipo_pagamento = "À vista"



        return tipo_pagamento, desconto if 'desconto' in locals() else acréscimo, total_final        


total = calcular_valor_final(total_do_pedido)

print("\n=== Pedidos realizados ===")
for item in Pedido_client:
    print(f"- {item}")
print(f"Total a pagar: R$ {total:.2f}")
print("=== FIM ===")