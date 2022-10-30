def validate_cpf(cpf):
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-','')

    if len(cpf) != 11:
        return 'Invalido'
    else:
        sum = 0
    for i in range(len(cpf)):
        sum += int(cpf[i])

    if sum == 33 or sum == 44 or sum == 55:
        return True
    else:
        return False 
class Alerts():  
    def alertSuccess(titulo,msg):
        alert={}
        alert['type']=1
        alert['title']=str(titulo)
        alert['text']=msg
        alert['icon']="success"
        return alert
    def alertError(titulo,msg):
        alert={}
        alert['type']=1
        alert['title']=str(titulo)
        alert['text']=msg
        alert['icon']="error"
        return alert
    def alertWarning(titulo,msg):
        alert={}
        alert['type']=1
        alert['title']=str(titulo)
        alert['text']=msg
        alert['icon']="warning"
        return alert