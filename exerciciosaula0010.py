from getpass import getpass
from mysql.connector import connect, Error

conexao =connect(
        host="localhost",
        user=input("Digite o  username do banco de dados: "),
        password=getpass("Digite a senha: "),
        database="teste")
    
class Cliente:
    def __init__(self,cpf,nome,email):
        self.cpf = cpf
        self.nome = nome
        self.email = email

def cadastro(self):
    cpf = input("Digite o seu cpf: ")
    nome = str(input("Digite o seu nome: "))
    email = str(input("Digite o seu email: "))
    query = """
    INSERT INTO Cliente (
    cpf,nome,
    email) VALUES ('"+cpf+"',"+nome+","+email+")
    """   
    cursor = conexao.cursor()
    cursor.execute(query)
    cursor.execute("commit") 

def consulta(self):
    query ="Select * from Cliente where nome like'"+ self.nome+"%';"
    cursor = conexao.cursor()   
    cursor.execute(query) 
    resultado =cursor.fetchall()
    print('Clientes: ')
    for db in resultado:
        print(db)

def excluir(self):
    nome=input("Digite o nome que quer apagar:")
    query= "delete from Cliente where nome=" +nome
    cursor.execute(query)
    cursor.execute("commit")

while True:
    opcao=int(input('''Cadastro de clientes
    [ 1 ] para cadastrar,
    [ 2 ] para consultar,
    [ 3 ] para excluir,
    [ 0 ] para sair.'''))
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        consulta()
    elif opcao == 3:
        excluir()
    elif opcao == 0:
        print("Muito Obrigado por ultilizar o meu sistema!Volte Sempre.")
        break
    else:
        print('Opção invalida tente novamente')
