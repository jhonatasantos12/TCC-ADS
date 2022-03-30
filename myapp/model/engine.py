import pyodbc
def retornar_conexao_sql():
    server = "LAPTOP-7R3VIR6J\ADS_TCC"
    database = "TCC-ADS/POG"#"TCC_ADS_POG" 
    username = "root"
    password = "admin"
    #string_conexao = 'Driver={Devart ODBC Driver for MySQL};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao
    
#cursor.execute("Insert into [dbo].[User] ([UserLogin],[UserEmail],[UserPassword]) VALUES ('?','?','?')")
#conexao.commit()


