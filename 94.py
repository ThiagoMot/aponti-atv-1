p1 = c = menor = total_de_gastos = 0
barato = ' '
while True:
    nome_produto = str(input('Digite o nome do Produto:')).strip().title()
    preço = int(input('Digite o valor do produto: '))
    c += 1
    if c == 1:
        menor = preço
        barato = nome_produto
    else:
        if preço < menor:
            menor = preço
            barato = nome_produto
    if preço >= 1000:
        p1 += 1
    total_de_gastos += preço
    q = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if q == 'N':
        break
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N]: ')).strip().upper()
print(f'O valor total da compra foi R${total_de_gastos:.2f}')
print(f'Temos {p1} produtos que custam mais ou igual a R$1000')
print(f'O produto mais barato é {barato} que custa R${menor}')