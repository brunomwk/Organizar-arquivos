import sys
import webbrowser

from gui_ferramentas import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from organizador import Organizar
from testador import Testar
from time import sleep


class Novo(QMainWindow, Ui_Dialog, Organizar, Testar):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.local = ''
        self.relatorio = list()
        self.btn_escolher_pasta.clicked.connect(self.escolher_pasta)
        self.btn_iniciar.clicked.connect(self.organizar_pasta)
        self.btn_abrir_relatorio.clicked.connect(self.open_relatorio)
        self.btn_teste_escolher_pasta.clicked.connect(self.teste_escolher_pasta)
        self.btn_iniciar_teste.clicked.connect(self.iniciar_teste)
        self.msg_sucesso.setText(' ')
        self.commandLinkButton.clicked.connect(self.abrir_insta)

    def abrir_insta(self):
        webbrowser.open('https://www.instagram.com/mwkbruno/')

    def escolher_pasta(self):
        self.local = QFileDialog.getExistingDirectory()
        print(self.local)

    def organizar_pasta(self):
        if len(self.local) == 0:
            print('selecione a pasta')
            self.msg_sucesso.setText('Selecione uma pasta')
        else:
            org = Organizar(self.local)
            org.organizando()
            self.msg_sucesso.setText('Pasta organizada com sucesso!')

    def open_relatorio(self):
        if len(self.local) == 0:
            self.msg_sucesso.setText('Selecione uma pasta')
        else:
            org = Organizar(self.local)
            org.abrir_relatorio()

    def teste_escolher_pasta(self):
        self.local = QFileDialog.getExistingDirectory()
        self.txt_escolha_uma_pasta.setText('')

    def iniciar_teste(self):
        local = self.local
        if len(local) == 0:
            self.txt_escolha_uma_pasta.setText('<= escolha uma pasta')
            print('escolha uma pasta para o teste')
        else:
            teste = Testar(local)
            teste.criar_pasta()

            for c in range(10):
                teste.testar_codigo()
                home = (local + f'\\teste_codigo')
                org = Organizar(home)
                org.organizando()
                if c == 9:
                    teste.msg_funcionando()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
