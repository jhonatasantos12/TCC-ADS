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

from django.core.paginator import Paginator
# Create your views here.

@login_required(redirect_field_name="register")
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
        }) 



def Listadepedidos(request):
    
    pedidos = PedidosModel.Pedido.objects.all().order_by('-data_registro')
    paginator = Paginator(pedidos,5)
    page = request.GET.get("pedidos")
    pedidos = paginator.get_page(page)
    return render(request,'pedidos/ListPedidos.html',
    context={
        "Pedidos":pedidos ,
        
    }) 
def pedidos(request):
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

@csrf_exempt
def entrada(request):
    alert ={}
    alert['messages']=[]
    Estoque = EstoqueModel.Estoque.objects.all()
    if request.method !='POST':
        for product in Estoque:
            if product.quantidade < product.min_prod:
                product_message = f"Alertamos que o produto {product.produto.nome},esta com quantidade abaixo do esperado em estoque"
                alert['messages'].append(product_message)
        if len(alert['messages']) < 1:
            return render (request,'pedidos/EntradaEstoque.html')
        return render (request,'pedidos/EntradaEstoque.html',context={"alert" :alert,"produtos": ProductModel.Product.objects.all()})
    quantidade = request.POST.get('qtd')
    produtoR = request.POST.get('product')
    try:
        tem = EstoqueModel.Estoque.objects.get(produto=produtoR)
    except:
        tem = None
    if tem == None:
        produtoC = ProductModel.Product.objects.get(id = produtoR)
        estoque = EstoqueModel.Estoque.objects.create(produto = produtoC, quantidade = quantidade)
        estoque.save()
    else:
        tem.quantidade  += int(quantidade)
        tem.save()
    return HttpResponse(produtoR,quantidade)


@login_required()
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
    #print(usuario.usuario.name)
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
        pedido = PedidosModel.Pedido.objects.create(Status= status,Atendente= usuario,tp_Pedido=1)
        pedido.save()
        for x in ProdPedido['Produtos']:
            produto = ProductModel.Product.objects.get(id= x)
            ProdutoPedido = PedidosModel.ProdutoPedido.objects.create(pedido = pedido, produto=produto,quantidade=ProdPedido['Produtos'][str(x)]['Quantidade'])
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