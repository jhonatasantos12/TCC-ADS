from flask import Flask,render_template, request
from model import engine
app = Flask(__name__)

@app.route("/AddProduct", methods =["GET","POST"])
def Add():
	resultado =''
	if request.method == "POST":
		name = request.form.get('product')
		value = request.form.get('value')
		resultado = engine.RegistryProduct(name,value)
	return render_template('registryProduct.html',resultado =resultado)


@app.route("/ListProduct", methods =["GET"])
def List():
	resultado = engine.AllProducts()
	return render_template('ListProducts.html',Products = resultado)


@app.route("/EditProduct/<int:id_product>", methods =["GET"])
def Edit(id_product):
	resultado = engine.Select(id_product)
	return str(resultado)	