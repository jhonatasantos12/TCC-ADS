import pyodbc
from model import engine

def RegistryProduct(name,value):
    sql ="Insert into [dbo].[product] ([name],[value]) VALUES (?,?)"
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql, (name,value))
    cursor.commit()
    return (name,"Cadastrado com sucesso")

def AllProducts():
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM [dbo].[product]")
    product = cursor.fetchall()
    mylist =[]
    for x in product:
        mylist.append(x)
    return mylist

def SelectProduct(id):
    sql = "Select name, value, id from [dbo].[product] where id = ?"
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql,id)
    product = cursor.fetchone()
    cursor.close()
    dic = {}
    dic['product'] = product[0]
    dic['value'] = product[1]
    dic['id']= product[2]
    return dic

def update(id,prod,val):
    sql = "UPDATE [dbo].[product] SET name= ? , value = ? where id = ?"
    conexao = engine.retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql,(prod,val,id))
    cursor.commit()
    cursor.close()
    return True