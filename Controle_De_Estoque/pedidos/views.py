from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from accounts.views import login
from product import models as ProductModel
from estoque import models as EstoqueModel
from customer import models as CustomerModel
from pedidos import models as PedidosModel
from worker  import models as WokerModel
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from utils import functions
from django.core.paginator import Paginator
# Create your views here.

@login_required()
def GetPedido(request,pedido_id):
    if request.method !='POST':
        Pedido = PedidosModel.Pedido.objects.get(id= pedido_id)
        
        ProdutosPedido = PedidosModel.ProdutoPedido.objects.filter(pedido = Pedido)
        if Pedido.Status.description == "Finalizado" or Pedido.Status.description == "Cancelado":
            alternable = False
        else:
            alternable = True
        #Categoria = PedidosModel.Categoria.objects.all()
        return render(request,'pedidos/PedidoGerado.html',
        context={
        'Pedido':Pedido,
        'ProdutosPedido':ProdutosPedido,
        'Categoria' :PedidosModel.Categoria.objects.all() ,
        'IsAlternable' : alternable,
        }) 
    status = request.POST.get('newStatus')
    pedido = PedidosModel.Pedido.objects.get(id= pedido_id)
    categoria = PedidosModel.Categoria.objects.get(id=status)
    pedido.Status = categoria
    pedido.save()
    alert = functions.Alerts.alertSuccess("Sucesso","Status de pedido alterado")
    Pedido = PedidosModel.Pedido.objects.get(id= pedido_id)
    ProdutosPedido = PedidosModel.ProdutoPedido.objects.filter(pedido = Pedido)
    if Pedido.Status.description == "Finalizado" or Pedido.Status.description == "Cancelado":
        alternable = False
    else:
        alternable = True
    return render(request,'pedidos/PedidoGerado.html',
        context={
        'Pedido':Pedido,
        'ProdutosPedido':ProdutosPedido,
        'Categoria' :PedidosModel.Categoria.objects.all() ,
        'IsAlternable' : alternable,
        "alert":alert
        }) 

def Listadepedidos(request):
    pedidos = PedidosModel.Pedido.objects.all().order_by('-data_registro')
    paginator = Paginator(pedidos,10)
    page = request.GET.get("pedidos")
    pedidos = paginator.get_page(page)
    return render(request,'pedidos/ListPedidos.html',
    context={
        "Pedidos":pedidos ,
        
    }) 

    if request.method !='POST':
        return render(request,'pedidos/StartPedido.html',
        context={
            "Customers": CustomerModel.Customer.objects.all(),
            "Estoque": EstoqueModel.Estoque.objects.all(),
        })
    cliente = request.POST.get('cliente')
    Estoque = EstoqueModel.Estoque.objects.all()
    ProdPedido= {}
    ProdPedido['Produtos'] ={}
    for x in Estoque:
        try:
            produto = request.POST.get(str(x.produto.id))
        except:
            produto = None
        if produto != None:
            limiteEstq = EstoqueModel.Estoque.objects.get(produto = x.produto.id)
            if int(produto) > limiteEstq.quantidade:
                return HttpResponse('Quantidade informada Indisponivel')
            ProdPedido['Produtos'][str(x.produto.id)] = {}
            ProdPedido['Produtos'][str(x.produto.id)]['Id'] = str(x.produto.id)
            ProdPedido['Produtos'][str(x.produto.id)]['NameProduct'] = str(x.produto.nome)
            ProdPedido['Produtos'][str(x.produto.id)]['Quantidade'] = produto
    if  ProdPedido['Produtos']:
        ProdPedido['Cliente'] =  cliente
        ProdPedido['Status'] = "Em Separação"
    else:
        print("Num tem produto bixo")
    Pcliente = CustomerModel.Customer.objects.get(id = ProdPedido['Cliente'])
    status = PedidosModel.Categoria.objects.get(id = 1)
    pedido = PedidosModel.Pedido.objects.create(Cliente = Pcliente, Status= status)
    pedido.save()
    for x in ProdPedido['Produtos']:
        produto = ProductModel.Product.objects.get(id= x)
        ProdutoPedido = PedidosModel.ProdutoPedido.objects.create(pedido = pedido, produto=produto,quantidade=ProdPedido['Produtos'][str(x)]['Quantidade'])
        ProdutoPedido.save()
        Estoque = EstoqueModel.Estoque.objects.get(produto = produto)
        Estoque.quantidade -= int(ProdPedido['Produtos'][str(x)]['Quantidade']) 
        Estoque.save()
    #PedidosModel.ProdutoPedido
    return render (request,'pedidos/StartPedido.html')

def opcoes(request):
    alert ={}
    alert['messages']=[]
    Estoque = EstoqueModel.Estoque.objects.all()
    if request.method !='POST':
        for product in Estoque:
            if product.quantidade < product.min_prod:
                product_message = f"Alertamos que o produto {product.produto.nome},esta com quantidade abaixo do esperado em estoque"
                alert['messages'].append(product_message)
        if len(alert['messages']) < 1:
            return render(request,'pedidos/opcoes.html')
    return render(request,'pedidos/opcoes.html',context={"alert" :alert})

@login_required(redirect_field_name='register')
def GerarPedido(request):
    if request.method !='POST':
        return render(request,'pedidos/GerarPedido.html',
        context={
            "Customers": CustomerModel.Customer.objects.all(),
            "Estoque": EstoqueModel.Estoque.objects.all(),
        })
    cliente = request.POST.get('cliente')
    user = request.POST.get('user')
    UserModel= User.objects.get(username = user)
    usuario =  WokerModel.Worker.objects.get(usuario = UserModel)
    if cliente != None:
        Estoque = EstoqueModel.Estoque.objects.all()
        ProdPedido= {}
        ProdPedido['Produtos'] ={}
        ProdPedido['Cliente'] =  cliente
        for x in Estoque:
            try:
                produto = request.POST.get(str(x.produto.id))
            except:
                produto = None
            if produto != None and int(produto) >0:
                limiteEstq = EstoqueModel.Estoque.objects.get(produto = x.produto.id)
                if int(produto) > limiteEstq.quantidade:
                    alert={}
                    alert['type']=1
                    alert['title']="Falha"
                    alert['text']="Você informou uma quantidade maior do que a disponivel em estoque "
                    alert['icon']="error"
                    return render (request,'pedidos/GerarPedido.html',
                    context={
                        "Customers": CustomerModel.Customer.objects.all(),
                        "Estoque": EstoqueModel.Estoque.objects.all(),
                        "Customer":CustomerModel.Customer.objects.get(id = cliente),
                        "alert":alert
                        })
                
                ProdPedido['Produtos'][str(x.produto.id)] = {}
                ProdPedido['Produtos'][str(x.produto.id)]['Id'] = str(x.produto.id)
                ProdPedido['Produtos'][str(x.produto.id)]['NameProduct'] = str(x.produto.nome)
                ProdPedido['Produtos'][str(x.produto.id)]['Quantidade'] = produto
        if  ProdPedido['Produtos']:
            tipo_Pedido = request.POST.get('tp_Pedido')
            if tipo_Pedido == None:
                alert={}
                alert['type']=1
                alert['title']="Falha"
                alert['text']="O pedido precisa ser registrado como venda ou locação"
                alert['icon']="error"
                return render (request,'pedidos/GerarPedido.html',
                context={
                    "Customers": CustomerModel.Customer.objects.all(),
                    "Estoque": EstoqueModel.Estoque.objects.all(),
                    "Customer":CustomerModel.Customer.objects.get(id = cliente),
                    "alert":alert
                    })
            ProdPedido['Status'] = "Em Separação"
            modelcliente = CustomerModel.Customer.objects.get(id = ProdPedido['Cliente'])
            status = PedidosModel.Categoria.objects.get(id = 1)
            tipo_Pedido=int(tipo_Pedido)
            pedido = PedidosModel.Pedido.objects.create(Cliente = modelcliente, Status= status,Atendente= usuario,tp_Pedido=tipo_Pedido)
            pedido.save()
            for x in ProdPedido['Produtos']:
                produto = ProductModel.Product.objects.get(id= x)
                ProdutoPedido = PedidosModel.ProdutoPedido.objects.create(pedido = pedido, produto=produto,quantidade=ProdPedido['Produtos'][str(x)]['Quantidade'])
                ProdutoPedido.save()
                Estoque = EstoqueModel.Estoque.objects.get(produto = produto)
                Estoque.quantidade -= int(ProdPedido['Produtos'][str(x)]['Quantidade']) 
                Estoque.save()
            alert = functions.Alerts.alertSuccess("Sucesso","Pedido registrado com sucesso")
            return render (request,'pedidos/GerarPedido.html',
            context={
                "alert":alert,
                "Customers": CustomerModel.Customer.objects.all(),
                "Estoque": EstoqueModel.Estoque.objects.all(),
                "Customer":CustomerModel.Customer.objects.get(id = cliente)
            })
        return render (request,'pedidos/GerarPedido.html',
            context={
                "Customers": CustomerModel.Customer.objects.all(),
                "Estoque": EstoqueModel.Estoque.objects.all(),
                "Customer":CustomerModel.Customer.objects.get(id = cliente)
            })
        
    return render (request,'pedidos/GerarPedido.html',
     context={
            "Customers": CustomerModel.Customer.objects.all(),
            "Estoque": EstoqueModel.Estoque.objects.all(),  
        })

def GerarEntrada(request):

    alert ={}
    alert['messages']=[]
    Estoque = EstoqueModel.Estoque.objects.all()
    if request.method !='POST':
        for product in Estoque:
            if product.quantidade < product.min_prod:
                product_message = f"Alertamos que o produto {product.produto.nome},esta com quantidade abaixo do esperado em estoque"
                alert['messages'].append(product_message)
        if len(alert['messages']) < 1:
            return render (request,'pedidos/GerarEntrada.html',context={
                "Estoque": EstoqueModel.Estoque.objects.all()
            })
        return render (request,'pedidos/GerarEntrada.html',context={
            "alert" :alert,
            "Estoque": EstoqueModel.Estoque.objects.all()
            })
    ProdPedido= {}
    ProdPedido['Produtos'] ={}
    user = request.POST.get('user')
    UserModel= User.objects.get(username = user)
    usuario =  WokerModel.Worker.objects.get(usuario = UserModel)
    for x in Estoque:
        try:
            produtoQtd = request.POST.get(str(x.produto.id))
        except:
            produtoQtd = None
        ProdPedido['Produtos'][str(x.produto.id)] = {}
        ProdPedido['Produtos'][str(x.produto.id)]['Id'] = str(x.produto.id)
        ProdPedido['Produtos'][str(x.produto.id)]['NameProduct'] = str(x.produto.nome)
        ProdPedido['Produtos'][str(x.produto.id)]['Quantidade'] = produtoQtd
    if  ProdPedido['Produtos']:
        status = PedidosModel.Categoria.objects.get(id = 5)
        pedido = PedidosModel.PedidoEntrada.objects.create(Status= status,Atendente= usuario)
        pedido.save()
        for x in ProdPedido['Produtos']:
            if  int(ProdPedido['Produtos'][str(x)]['Quantidade']) <=0:
                pass
            else:
                produto = ProductModel.Product.objects.get(id= x)
                ProdutoPedido = PedidosModel.ProdutoEntrada.objects.create(pedido = pedido, produto=produto,quantidade=ProdPedido['Produtos'][str(x)]['Quantidade'])
                ProdutoPedido.save()
                Estoque = EstoqueModel.Estoque.objects.get(produto = produto)
                Estoque.quantidade += int(ProdPedido['Produtos'][str(x)]['Quantidade']) 
                Estoque.save()
    alert={}
    alert['type']=1
    alert['title']="Sucesso"
    alert['text']=f"{UserModel} Entrada Registrada"
    alert['icon']="success"
    return render (request,'pedidos/GerarEntrada.html',context={
            "alert" :alert,
            "Estoque": EstoqueModel.Estoque.objects.all()
            })

def listaEntrada(request):
    pedidosEntrada = PedidosModel.PedidoEntrada.objects.all().order_by('-data_registro')
    paginator = Paginator(pedidosEntrada,10)
    page = request.GET.get("pedidos")
    pedidosEntrada = paginator.get_page(page)
    return render(request,'pedidos/ListaEntradas.html',
    context={
        "pedidosEntrada":pedidosEntrada ,
        
    }) 

def EntradaDetalhes(request,pedido_id):
    Pedido = PedidosModel.PedidoEntrada.objects.get(id= pedido_id)  
    ProdutosEntrada = PedidosModel.ProdutoEntrada.objects.filter(pedido = Pedido)
    return render(request,'pedidos/EntradaDetalhes.html',
    context={
    'Pedido':Pedido,
    'ProdutosEntrada':ProdutosEntrada,
    }) 

def SemPermisao(request):
    return render (request,'pedidos/SemPermissao.html')