def leiaInt(msg):
    """Lê um número inteiro

    Args:
        msg (str): mensagem que será mostrada para o usuário

    Returns:
        int: retorna um número inteiro
    """
    while True:
        lei = input(msg)
        try:
            lei = int(lei)
        except ValueError:
            print('\033[31mErro!! Digite um número inteiro válido!\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro!! O usuário não informou este número.')
            return 0
        else:
            return lei
def leiaFloat(msg):
    """Função que lê um número real

    Args:
        msg (str): mensagem que será mostrada ao usuário

    Returns:
        float: número real que será mostrado ao usuário
    """
    lei = input(msg)
    while True:
        try:
            lei = float(lei)
        except (ValueError, TypeError):
            print('\033[31mErro!! Tipo não válido, por favor, digite um número real válido!!\033[m')
        except KeyboardInterrupt:
            print('\033[31mErro!! O usuário não informou o número!')
            return 0
        except:
            print('\033[31mErro! Por favor, tente novamente!')
        else:
            return lei
a = leiaInt('Digite um número inteiro: ')
b = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {a} e o número real foi {b}')