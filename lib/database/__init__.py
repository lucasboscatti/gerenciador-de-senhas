import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('userPasswords.db')
        self.cursor = self.conn.cursor()
    
    def acessPasswordsUser(self):
        try:
            self.cursor.execute(f'''CREATE TABLE user(username,userpass)''')
        except sqlite3.OperationalError:
            return False
        else:
            return True
    
    def dataUser(self, login, password):
        self.cursor.execute(f"INSERT INTO user(username,userpass) VALUES (?,?)", (login, password))
        self.conn.commit()
    
    def createUser(self):
        while True:
            registerUsername = str(input('Digite seu nome de usuário: ')).strip()
            exist = self.checkUser(registerUsername)
            if not exist:
                confirmUsername = str(input(f'Deseja confirmar {registerUsername}? (S/N)')).upper()
                if confirmUsername in ['N', 'NÃO', 'NAO']:
                    continue
                elif confirmUsername in ['S', 'SIM']:
                    while True:
                        registerUserpassword = str(input('Digite uma senha: '))
                        confirmUserpassword = str(input('Confirme sua senha: '))
                        if registerUserpassword == confirmUserpassword:
                            self.dataUser(registerUsername, registerUserpassword)
                            self.cursor.execute(f'''CREATE TABLE {registerUsername}passwords(account,login,password)''')
                            print('Conta criada com sucesso!')
                            break
                        else:
                            print('\033[1;31mAs senhas são incompatíveis!\033[m')
                    break
                else:
                    print('\033[1;31mDigite apenas SIM ou NÃO (S/N)!\033[m')
            elif exist > 0:
                print(f'Usuário {registerUsername} já existe!')
    
    def checkUser(self, user):
        self.cursor.execute(f'SELECT * FROM user')
        for row in self.cursor:
            if row[0] == user:
                return True
        return False

    def checkPassword(self, password):
        self.cursor.execute(f'SELECT * FROM user')
        for row in self.cursor:
            if row[1] == password:
                return True
        return False

    def insertData(self, user, account,login,password):
        self.cursor.execute(f"INSERT INTO {user}passwords(account,login,password) VALUES (?,?,?)", (account,login,password))
        self.conn.commit()

    def readData(self, user, account):
        self.cursor.execute(f'SELECT * from {user}passwords')
        for row in self.cursor:
            if row[0] == account:
                print(f'Login = {row[1]}\nSenha = {row[2]}')

    def checkData(self, txt, user):
        while True:
            account = str(input(txt)).upper().strip()
            self.cursor.execute(f'SELECT * FROM {user}passwords')
            for row in self.cursor:
                if row[0] == account:
                    return account
            else:
                print(f"\033[1;31mERRO! Digite uma conta existente no gerenciador.\033[m")

    def showData(self, user):
        self.cursor.execute(f'SELECT * from {user}passwords')
        data = self.cursor.fetchall()
        if len(data) == 0:
            return True
        else:
            for row in data:
                print(row[0])
  
    def deleteData(self, user, account):
        self.cursor.execute(f'''DELETE FROM {user}passwords WHERE account=?''', (account,))
        print(f'conta do {account} deletada com sucesso!')
        self.conn.commit()

    def rectify(self, txt):
        while True:
            name = str(input(txt)).strip()
            confirm = str(input('Deseja confirmar essa informação? (S/N) ')).upper().strip()
            if confirm in ['S', 'SIM']:
                return name
            elif confirm in ['N', 'NÃO', 'NAO']:
                continue
            else:
                print(f'\033[1;31mERRO! Digite apenas SIM ou NÃO (S/N)!\033[m')

    def disconnect(self):
        self.conn.close()
