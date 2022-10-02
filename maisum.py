flag = 1
while flag != 0: 
    obter = int(input('''Menu de opções!!
    1 para cadrastro no my sql
    2 para consultar tabela
    3 excluir algun dado 
    0 para sair'''))
    if obter == 1:
        cadastro()
    elif obter == 2:
        consulta()
    elif obter == 3:
        excluir()
    elif obter == 0:
        break
    else:
        print("opção inválida")


    def cadastro():
        conexão = connect(
            host="localhost",
            user=input("Enter username: "),
            password=getpass("Enter password: "),
            database="teste",
        )
    def consulta():
        consultar_tabela = "Select * from filmes"
        with connection.cursor() as cursor:
            cursor.execute(consultar_tabela)
            for  db in cursor:
                print(db)


    
    
    
    
  

