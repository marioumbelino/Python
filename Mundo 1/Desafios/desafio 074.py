from random import randint
ale = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram {ale}')
print(f'O maior número sorteado foi {max(ale)}')
print(f'O menor número sorteado foi {min(ale)}')
