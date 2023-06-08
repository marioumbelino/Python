soma = count = 0
while True:
    num = int(input('Digite um número [digite "999" para parar]: '))
    if num == 999:
        break
    count += 1
    soma += num
print(f'Você digitou {count} números. A soma destes números resulta em {soma}.')