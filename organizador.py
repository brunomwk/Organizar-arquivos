from os import listdir, path, mkdir, rename, system
import shutil
from os.path import isfile, join, expanduser
from datetime import datetime


class Organizar:
    time = datetime.now()

    def __init__(self, local):
        self.local = local
        # recebendo somente os arquivos da pasta downloads
        self.lendo = [arqv for arqv in listdir(self.local) if isfile(join(self.local, arqv))]
        self.relatorio = ["RELATÓRIO:", " "]
        self.pasta_relatorio = self.local + f'\\relatorio'
        self.data = Organizar.time.strftime('%d-%m-%Y_%H-%M-%S')
        self.novo_relatorio = f'{self.pasta_relatorio}\\{self.data}.txt'


    def organizando(self):
        pasta_criada = 0
        arquivos_movidos = 0
        print('ANALISANDO OS ARQUIVOS')
        if len(self.lendo) == 0:
            self.relatorio.append(f"A pasta {self.local} não tem arquivos,"
                                  f" somente pastas. Nenhum serviço foi executado")
            # print('pasta vazia')
        else:
            for c in range(len(self.lendo)):
                analise = self.lendo[c].split('.')
                # criar pasta da extensao caso nao exista
                if not path.exists(self.pasta_relatorio):
                    mkdir(self.pasta_relatorio)
                if not path.exists(self.local + f'\\{analise[-1]}'):
                    mkdir(self.local + f'\\{analise[-1]}')
                    self.relatorio.append(f"'pasta criada criado para os arquivos {analise[-1]} ")
                    pasta_criada += 1
                try:
                    # mover o arquivo para a pasta da sua extensao
                    shutil.move(self.local + f'\\{self.lendo[c]}', self.local + f'\\{analise[-1]}')
                    self.relatorio.append(f'arquivo {self.lendo[c]} '
                                          f'foi movido para a pasta {self.local}\\{analise[-1]}')
                    arquivos_movidos += 1
                except shutil.Error:
                    local_verificar = self.local + f'\\{analise[-1]}'
                    verificando = [arqv for arqv in listdir(local_verificar) if isfile(join(local_verificar, arqv))]
                    # condicao criada para verificar se ja existe o arquivo(1) para enumerar os arqv repetidos
                    if f'{analise[0]}-_-(1.{analise[-1]}' not in verificando:
                        # print(f'não existe o arquivo {self.lendo[c]}(1) na pasta')
                        rename(self.local + f'\\{self.lendo[c]}', self.local + f'\\{analise[0]}-_-(1.{analise[-1]}')
                        shutil.move(self.local + f'\\{analise[0]}-_-(1.{analise[-1]}', self.local + f'\\{analise[-1]}')
                        self.relatorio.append(f'ja existe um arquivo com o nome {self.lendo[c]}na pasta {analise[-1]}  '
                                              f', ele foi renomeado para {analise[0]}(1).{analise[-1]}  ')
                        arquivos_movidos += 1
                    else:  # O ERRO TA NESSE ELSE  EEEEEEEEEEEEEEEEEEEEE
                        analisar = f"{self.local}\\{analise[-1]}"
                        pasta_analisar = [arqv for arqv in listdir(analisar) if isfile(join(analisar, arqv))]
                        arquivo_analisar = list()
                        for cont in range(len(pasta_analisar)):
                            if analise[0] in pasta_analisar[cont]:
                                try:
                                    arquivo_analisar.append(int(pasta_analisar[cont]
                                                                .rstrip(f'.{analise[-1]}').split('-_-(')[-1]))
                                    arquivos_movidos += 1
                                except ValueError:
                                    pass
                        novo_nome = f"{analise[0]}-_-({max(arquivo_analisar) + 1}.{analise[-1]}"
                        rename(self.local + f'\\{self.lendo[c]}', self.local + f'\\{novo_nome}')
                        try:
                            shutil.move(self.local + f'\\{novo_nome}', self.local + f'\\{analise[-1]}')
                            self.relatorio.append(f'Existe um arquivo com o nome {self.lendo[c]} na pasta {analise[-1]}'
                                                  f', ele foi renomeado para {novo_nome}  ')
                            arquivos_movidos += 1
                        except shutil.Error:
                            novo_nome2 = f"{analise[0]}-_-({max(arquivo_analisar) + 2}.{analise[-1]}"
                            rename(self.local + f'\\{novo_nome}', self.local + f'\\{novo_nome2}')
                            shutil.move(self.local + f'\\{novo_nome2}', self.local + f'\\{analise[-1]}')
                            arquivos_movidos += 1

        self.relatorio.append(f'Arquivos movidos:  {arquivos_movidos}  ')
        self.relatorio.append(f'Pastas criadas:  {pasta_criada}  ')
        with open(self.novo_relatorio, 'a') as arquivo:
            if len(self.relatorio) == 0:
                arquivo.write('Não foi localizado nenhum arquivo fora da pasta de sua extensão')
            else:
                for linha in self.relatorio:
                    arquivo.write(linha + '\n')

    def abrir_relatorio(self):
        system(f'start {path.realpath(self.novo_relatorio)}')

"""
home = expanduser("~\\downloads")
org = Organizar(home)
org.organizando()
org.abrir_relatorio()
"""