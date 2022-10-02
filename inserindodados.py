from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="teste4",
    ) as connection:       
        create_movies_table_query = """
        INSERT INTO filmes (
            id, 
            titulo,
            anodelancamento,
            sexo,
            collecao) 
            VALUES (
            1, 
            "o vento levou",
            12/05/2022,
            m,
            tarantino)
        )"""
