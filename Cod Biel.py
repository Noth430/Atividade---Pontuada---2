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

Codigo_Prato =(input("Digite o Código do seu Prato: "))



resultado = 0

match(Codigo_Prato):
    case "1":
        print("Picanha R$ 100,00")
    case "2":
        print("Strognoff R$35,00")
    case "3":
        print("Lasanha R$35,00")
    case "4":
        print("Frango a Milanesa R$70,00")
    case "5":
        print("Peixe Grelhado R$60,00")
    case "6":
        print("Burrito com Fritas R$85,00")
    case "7":
        print("Hamburguer R$25,00")
    case "0":
        print("Opção invalida, Por favor digite um Código Valido.")


print,("=== FIM ===")      