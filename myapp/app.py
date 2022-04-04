from flask import Flask, redirect,render_template, request
from model import ProductEngine
from model import WorkerEngine
app = Flask(__name__)

#---Produtos---
@app.route("/AddProduct", methods =["GET","POST"])
def AddProduct():
	resultado =''
	if request.method == "POST":
		name = request.form.get('product')
		value = request.form.get('value')
		resultado = ProductEngine.RegistryProduct(name,value)
	return render_template('product/registryProduct.html',resultado =resultado)


@app.route("/ListProduct", methods =["GET"])
def ListProduct():
	resultado = ProductEngine.AllProducts()
	return render_template('product/ListProducts.html',Products = resultado)


@app.route("/EditProduct/<int:id_product>", methods =["GET","POST"])
def EditProduct(id_product):
	resultado = ProductEngine.SelectProduct(id_product)
	if request.method == "POST":
		name = request.form.get('product')
		value = request.form.get('value')
		result = ProductEngine.update(id_product,name,value)
		if result  == True:
			return redirect("ListProducts.html")
	if resultado == None:
		return render_template('NotFound.html') #ProdutoNãoEncontrado Configurar ViewError 
	return render_template("product/EditProduct.html",resultado = resultado)


#---Funcionarios---

@app.route("/AddWorker", methods = ['GET','POST'])
def AddWorker():
	if request.method =="POST":
		nome = request.form.get("name")
		sobrenome = request.form.get("last_name")
		cpf = request.form.get("cpf")
		telefone = request.form.get("PhoneNumber")
		cargo = request.form.get("office")
		WorkerEngine.RegistryWorker(nome,sobrenome,cpf,telefone,cargo)
		return redirect("www.google.com")
	return render_template("Worker/AddWorker.html")

@app.route("/WorkersList", methods =["GET"])
def ListWorkers():
	resultado = WorkerEngine.AllWorkers()
	return render_template('Worker/ListWorkers.html',Workers = resultado)