from lib.interface import Interface
from lib.database import Database


def interface():
    itr.header('GERENCIADOR DE SENHAS')       
    while True:
        user = str(input(f'{itr.cor(3)}Login {itr.cor(4)}(0 para criar nova conta){itr.cor(0)}: '))   
        if user == '0':
            bd.createUser()        
        else:
            checkuser = bd.checkUser(user)
            if checkuser:
                while True:
                    password = str(input(f'{itr.cor(3)}Senha{itr.cor(0)}: '))
                    checkpass = bd.checkPassword(password)
                    if checkpass:
                        break
                    else:
                        print(f'{itr.cor(1)}Senha incorreta! Tente novamente.{itr.cor(0)}')
                        continue
                break
            else:
                print(f'{itr.cor(1)}Usuário não encontrado ou erro de digitação.{itr.cor(0)}')
                continue          
    itr.header(f'{itr.cor(3)}BEM VINDO {user.upper()}!{itr.cor(0)}')    
    while True:
        itr.menu()
        print(itr.line())
        d = options(f'{itr.cor(3)}SUA OPÇÃO:{itr.cor(0)} ', user)
        print(itr.line()) 
        if d == 'disconnect':
            break


def options(txt, user):
    while True:        
        op = str(input(txt)).strip()
        print(itr.line())             
        if op not in ['1', '2', '3', '4', '5']:
            print(f'{itr.cor(1)}ERRO! Digite uma opção válida!{itr.cor(0)}')                    
        else:
            if op == '1':
                itr.line()
                account = bd.rectify('Nome da conta: ')
                login = bd.rectify('Login: ')
                password = bd.rectify('Senha: ')
                itr.line()
                bd.insertData(user, account.upper(), login, password)
                print(f'Conta {account} salva com sucesso!')              
            elif op == '2':
                vallidation = bd.showData(user) 
                if vallidation:
                    print('Ainda não há contas cadastradas!')
                else:
                    print(itr.line()) 
                    conta = bd.checkData('Você quer informação de qual conta? ', user)
                    print(itr.line()) 
                    bd.readData(user, conta)                  
            elif op == '3':
                vallidation = bd.showData(user)
                if vallidation:
                    print('Ainda não há contas cadastradas!')                 
            elif op == '4':
                vallidation = bd.showData(user)
                if vallidation:
                    print('Ainda não há contas cadastradas!')
                else:
                    print(itr.line()) 
                    account = bd.checkData('Você quer deletar qual conta? ', user)
                    print(itr.line()) 
                    bd.deleteData(user, account)            
            elif op == '5':
                print('Sessão encerrada!')
                return 'disconnect'
            break
        
        
def main():
    bd.acessPasswordsUser()
    interface()
    bd.disconnect()


if __name__ == '__main__':
    bd = Database()
    itr = Interface()
    main()