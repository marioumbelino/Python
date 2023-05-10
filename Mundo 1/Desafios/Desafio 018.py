import math
an = float(input('Digite um valor de um ângulo em graus: '))
rad = math.radians(an)
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)
print('Pra o ângulo \033[31m{}\033[m temos o seno \033[36m{:.2f}\033[m, o cosseno \033[36m{:.2f}\033[m e a tangente \033[36m{:.2f}\033[m.'.format(an, s, c, t))