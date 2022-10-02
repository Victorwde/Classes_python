from getpass import getpass
from mysql.connector import connect, Error

conexao =connect(
        host="localhost",
        user=input("Digite o  username do banco de dados: "),
        password=getpass("Digite a senha: "),
        database="teste")

while True:
    nome = input("Digite o nome do cliente: ")
    nasc = int(input("Digite a data de nascimento: "))
    tel = int(input("Digite o telefone para contato: "))
    query = """
    INSERT INTO Cliente (
    nome,data_nascimento,
    telefone) VALUES ('"+nome+"',"+nasc+","+tel+")
    """   
    cursor = conexao.cursor()
    cursor.execute(query)
    cursor.execute("commit") 
    sair = int(input('''Para sair digite 0,
    1 para excluir um cliente,
    ou 2 para consultar a tabela:'''))
    if sair == 0:
        break
    elif sair == 1:
        a=input("Digite o nome que quer apagar:")
        query= "delete from Cliente where nome=" +nome
        cursor.execute(query)
        cursor.execute("commit")
    elif sair == 2:
        aa=input("digite o nome do Cliente a pesquisar")
        query ="Select * from Cliente where nome like'"+ aa+"%';"
        cursor = conexao.cursor()   
        cursor.execute(query) 
        resultado =cursor.fetchall()
        print('Clientes: ')
        for db in resultado:
            print(db)
    else:
        print('OPÇÃO INVÁLIDA')
        break


