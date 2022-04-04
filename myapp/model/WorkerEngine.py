import pyodbc
from model import engine
def RegistryWorker(name,last_name,cpf,PhoneNumber,Office):
    sql ="Insert into [dbo].[Worker] ([name],[last_name],[cpf],[PhoneNumber],[office]) VALUES (?,?,?,?,?)"
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql, (name,last_name,cpf,PhoneNumber,Office))
    cursor.commit()
    return True
def AllWorkers():
    sql ="SELECT * FROM [dbo].[Worker]"
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql)
    Workers = cursor.fetchall()
    mylist =[]
    for x in Workers:
        mylist.append(x)
    return mylist