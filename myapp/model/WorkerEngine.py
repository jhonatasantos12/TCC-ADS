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

def SelectWorkers(id):
    sql = "Select name,last_name,cpf,PhoneNumber,Office,id from [dbo].[Worker] where id = ?"
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql,id)
    Worker = cursor.fetchone()
    cursor.close()
    dic = {}
    dic['name'] = Worker[0]
    dic['last_name'] = Worker[1]
    dic['cpf']= Worker[2]
    dic['PhoneNumber']= Worker[3]
    dic['Office'] = Worker[4]
    dic['id'] = Worker[5] 
    return Worker
def EditWorker(name,last_name,cpf,PhoneNumber,Office,Id):
    sql = "UPDATE [dbo].[Worker] SET name= ?, last_name = ?, cpf = ?, PhoneNumber =? , office = ?  where id = ?"
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql,(name,last_name,cpf,PhoneNumber,Office,Id))
    cursor.commit()
    cursor.close()
    return True 