import pyodbc
def retornar_conexao_sql():
    server = "LAPTOP-7R3VIR6J\ADS_TCC"
    database = "TCC-ADS/POG"
    #username = "aula_mongodb"
    #password = "abc123"
    #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao
    
#cursor.execute("Insert into [dbo].[User] ([UserLogin],[UserEmail],[UserPassword]) VALUES ('?','?','?')")
#conexao.commit()

def RegistryProduct(name,value):
    sql ="Insert into [dbo].[product] ([name],[value]) VALUES (?,?)"
    conexao = retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql, (name,value))
    cursor.commit()
    return (name,"Cadastrado com sucesso")

def AllProducts():
    conexao = retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM [dbo].[product]")
    product = cursor.fetchall()
    mylist =[]
    for x in product:
        mylist.append(x)
    return mylist

def Select(id):
    sql = "Select name, value from [dbo].[product] where id = ?"
    conexao = retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql,id)
    product = cursor.fetchone()
    cursor.close()
    return product
