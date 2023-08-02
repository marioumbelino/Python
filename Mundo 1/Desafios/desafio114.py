import urllib
import urllib.request

try:
    teste = urllib.request.urlopen('https://pudim.com.br/')
except urllib.error.URLError as erro:
    print('\033[31mNão foi possível acessar o site, tente novamente!\033[m')
else:
    print('Consegui acessar o site!')