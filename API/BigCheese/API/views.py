from django.shortcuts import redirect, render
from API.models import Produto, Venda, Produtos_Das_Vendas
from API.form import produtoForm, vendaForm

# Create your views here.

#View da página inicial
def index(request):
    return render(request, "index.html")

def TabelaProdutos(request):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        form = produtoForm(request.POST)
        if form.is_valid():
            form.save()
            form = produtoForm()
    else:
        form = produtoForm()
    return render(request, 'tabelaProdutos.html', {'form': form, 'produtos': produtos})

def editarProduto(request, id):
    produto = Produto.objects.get(pk=id)
    produtos = Produto.objects.all()
    form = produtoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        form = produtoForm()
        return redirect('tabelaProdutos')
    return render(request, 'tabelaProdutos.html', {'form': form, 'produtos': produtos})

def deletarProduto(request, id):
    produto = Produto.objects.get(pk=id)
    produto.delete()
    return redirect("tabelaProdutos")


def cadastrarVenda(request):
    form = vendaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        descricao = form.cleaned_data['descricao']

        # Criação da venda com um valor inicial de ven_precoTotal
        venda, created = Venda.objects.get_or_create(ven_desc=descricao, defaults={'ven_precoTotal': 0.0})

        # Processamento dos produtos selecionados no formulário
        for produto in form.cleaned_data['produtos']:
            quantidade_field_name = f'quantidade_{produto.id}'
            quantidade = form.cleaned_data.get(quantidade_field_name, 0)

            # Criação ou atualização do item de venda associado a este produto
            item_venda, created = Produtos_Das_Vendas.objects.get_or_create(pdv_pro=produto, pdv_ven=venda)
            item_venda.pdv_qtd += quantidade
            item_venda.pdv_PrecoTotalItem += quantidade * produto.pro_preco
            item_venda.save()

            # Atualização do preço total da venda
            venda.ven_precoTotal += item_venda.pdv_PrecoTotalItem

        # Salvando a venda
        venda.save()

        return redirect('tabelaVendas')

    vendas = Venda.objects.all()
    return render(request, 'tabelaVendas.html', {'form': form, 'vendas': vendas})