valor = float(input('Me informe o valor do produto: R$'))
forma = str(input('Me informe a forma de pagamento: ')).upper()
if 'CARTÃO' in forma or 'CARTAO' in forma:
    parc = str(input('Me informe se é à vista ou em quantas parcelas: ')).upper()
    if '2' in parc or 'DUAS' in parc or 'DOIS' in parc:
        print('Pagando em 2x no cartão, o valor permanece igual. \nSendo assim, você pagará em duas parcelas de R${:.2f} e seu valor final é igual a R${:.2f}'.format((valor / 2), valor))
    elif 'vista' in parc or '1' in parc or 'uma' in parc:
        vis = valor - (valor * 5 / 100)
        print('Pagando à vista no cartão, você consegue um desconto de 5%. \nSendo assim, você pagará R${:.2f} no produto'.format(vis))
    else:
        jur = valor + (valor * 20 / 100)
        print('Para parcelas de 3x ou mais, você pagará um juros de 20% no valor total do produto. \nAssim, você pagará R${:.2f} no total pelo produto!'.format(jur))
elif 'DINHEIRO' in forma or 'CHEQUE' in forma or 'PIX' in forma:
    desc = valor - (valor * 10 / 100)
    print('Pagando em dinheiro, cheque ou pix, você ganha um desconto de 10% no valor total do produto. \nAssim, você pagará um total de R${:.2f} pelo produto!'.format(desc))
        