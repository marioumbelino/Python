# Rascunho próprio
"""lanche = ['pizza', 'hambúrguer', 'suco', 'pudim']
print(lanche)
lanche.append('cookie')
lanche[2] = 'refrigerante'
lanche.insert(0, 'sorvete')
lanche.insert(2, 'batata frita')
print(lanche)
lanche.pop(4)
print(lanche)
print(lanche)
if 'batata frita' in lanche:
    lanche.remove('batata frita')
print(lanche)
val = list(range(1, 5))
print(val)"""

# Rascunho da Aula
'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
while 2 in num:
    num.remove(2)
print(num)
print(f'Esta lista tem {len(num)} elementos.')'''

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print('Os valores são:', end=' ')
for v in valores:
    print(v, end=' ')
print('\nEm suas posições, respectivamente:', end=' ')
for c, v1 in enumerate(valores):
    print(c, end=' ')
print('\nFim da lista!!')
