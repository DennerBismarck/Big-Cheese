from django.shortcuts import redirect, render
from API.models import Produto, Venda, Produtos_Das_Vendas
from API.form import produtoForm, vendaForm
from django.db.models import Sum, Count

# Create your views here.

#View da página inicial
def index(request):
    qtd_ganho_total = Venda.objects.filter(ven_pago='Pagou').aggregate(Sum('ven_precoTotal'))['ven_precoTotal__sum'] or 0

    vendas_nao_pagas = Venda.objects.filter(ven_pago='Não pagou')

    produtos_mais_vendidos = Produto.objects.annotate(total_vendido=Count('venda__produtos_das_vendas')).order_by('-total_vendido')

    context = {
        'qtd_ganho_total': qtd_ganho_total,
        'vendas_nao_pagas': vendas_nao_pagas,
        'produtos_mais_vendidos': produtos_mais_vendidos,
    }

    return render(request, "index.html", context)

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
        pag_status = form.cleaned_data['pagou']
        # Criação da venda com um valor inicial de ven_precoTotal
        venda, created = Venda.objects.get_or_create(ven_desc=descricao, defaults={'ven_precoTotal': 0.0})
        venda.ven_pago = pag_status
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

def editarvenda(request, id):
    venda = Venda.objects.get(pk=id)
    vendas = Venda.objects.all()

    # Inicialize o formulário com dados existentes da venda
    form = vendaForm(request.POST or None, initial={
        'descricao': venda.ven_desc,
        'pagou': venda.ven_pago,
        # Adicione outros campos do formulário aqui
    })

    if request.method == 'POST' and form.is_valid():
        # Limpa os itens de venda associados a esta venda
        venda.produtos_das_vendas_set.all().delete()

        # Processamento dos produtos selecionados no formulário
        for produto in form.cleaned_data['produtos']:
            quantidade_field_name = f'quantidade_{produto.id}'
            quantidade = form.cleaned_data.get(quantidade_field_name, 0)

            # Criação do novo item de venda associado a este produto
            item_venda = Produtos_Das_Vendas.objects.create(
                pdv_pro=produto,
                pdv_ven=venda,
                pdv_qtd=quantidade,
                pdv_PrecoTotalItem=quantidade * produto.pro_preco
            )

        # Atualiza outros campos da venda
        venda.ven_desc = form.cleaned_data['descricao']
        venda.ven_pago = form.cleaned_data['pagou']

        # Atualização do preço total da venda
        venda.ven_precoTotal = venda.produtos_das_vendas_set.aggregate(Sum('pdv_PrecoTotalItem'))['pdv_PrecoTotalItem__sum'] or 0

        # Salvando a venda
        venda.save()

        return redirect('tabelaVendas')

    return render(request, 'tabelaVendas.html', {'form': form, 'vendas': vendas})


def deletarvenda(request, id):
    venda = Venda.objects.get(pk=id)
    venda.delete()
    return redirect('tabelaVendas')