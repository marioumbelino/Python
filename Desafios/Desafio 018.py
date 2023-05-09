import math
an = float(input('Digite um valor de um ângulo em graus: '))
rad = math.radians(an)
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)
print('Pra o ângulo {} temos o seno {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'.format(an, s, c, t))