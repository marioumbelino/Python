import datetime
ano = int(input('Digite o ano desejado '))
di = datetime.date(ano, 1, 1)
df = datetime.date(ano + 1, 1, 1)
dife = df - di
dias = dife.days
if dias > 365:
    print('O ano de {} é um ano bisexto, pois possui 366 dias'.format(ano))
else:
    print('O ano de {} não é um ano bisexto, pois possui 365 dias'.format(ano))
