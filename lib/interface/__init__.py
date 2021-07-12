class Interface:
    def line(self, length=50):
        return '-' * length

    def header(self, txt):
        print(self.line())
        print(txt.center(50))
        print(self.line())

    def menu(self):
        print(f'''{self.cor(3)}1{self.cor(0)} -{self.cor(4)} Adicionar nova conta
{self.cor(3)}2{self.cor(0)} -{self.cor(4)} Resgatar os dados de uma conta
{self.cor(3)}3{self.cor(0)} -{self.cor(4)} Ver contas cadastradas
{self.cor(3)}4{self.cor(0)} -{self.cor(4)} Deletar uma conta
{self.cor(3)}5{self.cor(0)} -{self.cor(4)} Sair do gerenciador de senhas{self.cor(0)}''')

    def cor(self, nome):
        cores = {'0': '\033[m',     # 0 - sem cores
                '1': '\033[1;31m',  # 1 - vermelho
                '2': '\033[1;32m',  # 2 - verde
                '3': '\033[1;33m',  # 3 - amarelo
                '4': '\033[1;34m',  # 4 - azul
                '5': '\033[1;35m',  # 5 - roxo
                '6': '\033[7;30m'   # 6 - branco
                }
        return cores[f'{nome}']


