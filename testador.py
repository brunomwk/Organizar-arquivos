import os
from os import mkdir
from os.path import expanduser
from organizador import Organizar
from random import randint


class Testar:
    def __init__(self, localizacao):
        self.local = localizacao
        self.pasta_teste = localizacao + f'\\teste_codigo'

    def criar_pasta(self):
        try:
            mkdir(self.pasta_teste)
        except FileExistsError:
            pass

    def testar_codigo(self):

        for contador in range(1, 2):
            with open(f'{self.pasta_teste}\\teste{contador}.txt', 'w') as arquivo:
                arquivo.write('teste')
            with open(f'{self.pasta_teste}\\teste{contador}.csv', 'w') as arquivo:
                arquivo.write('teste')
            with open(f'{self.pasta_teste}\\teste{contador}.xls', 'w') as arquivo:
                arquivo.write('teste')
            with open(f'{self.pasta_teste}\\teste{contador}.jpg', 'w') as arquivo:
                arquivo.write('teste')

    def msg_funcionando(self):
        with open(f'{self.pasta_teste}\\O PROGRAMA ESTA FUNCIONANDO!!!.txt', 'w') as arquivo:
            arquivo.write(f'O PROGRAMA ESTA FUNCIONANDO!!{randint(1, 1000)}')
            os.system(f'start {os.path.realpath(self.pasta_teste)}')

"""
local = expanduser("~\\downloads")
teste = Testar(local)
teste.criar_pasta()

for c in range(10):
    teste.testar_codigo()
    home = expanduser("~\\downloads" + f'\\teste_codigo')
    org = Organizar(home)
    org.organizando()
    if c == 9:
        teste.msg_funcionando()
"""


