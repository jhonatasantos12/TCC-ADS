import pyodbc
from model import engine
def RegistryWorker(name,last_name,cpf,PhoneNumber,Office):
    sql ="Insert into [dbo].[Worker] ([name],[last_name],[cpf],[PhoneNumber],[office]) VALUES (?,?,?,?,?)"
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql, (name,last_name,cpf,PhoneNumber,Office))
    cursor.commit()
    return True