from flask import Flask, redirect,render_template, request
from model import ProductEngine
app = Flask(__name__)

@app.route("/AddProduct", methods =["GET","POST"])
def Add():
	resultado =''
	if request.method == "POST":
		name = request.form.get('product')
		value = request.form.get('value')
		resultado = ProductEngine.RegistryProduct(name,value)
	return render_template('product/registryProduct.html',resultado =resultado)


@app.route("/ListProduct", methods =["GET"])
def List():
	resultado = ProductEngine.AllProducts()
	return render_template('product/ListProducts.html',Products = resultado)


@app.route("/EditProduct/<int:id_product>", methods =["GET","POST"])
def Edit(id_product):
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