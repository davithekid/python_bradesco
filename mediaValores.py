qtd = 0
soma = 0
media = 0
valor= float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    valor = float(input("Digite um valor: "))

    media = soma/qtd
    print("\nTotal da soma: ", soma)
    print("\nQuantidade de valores digitados: ", qtd)
    print("\nMédia de valores: ", media)
