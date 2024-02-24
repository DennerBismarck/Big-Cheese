from django.forms import ModelForm
from API.models import Produto, Venda, Produtos_Das_Vendas
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class produtoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["pro_desc", "pro_preco"]

class vendaForm(forms.Form):
    produtos = forms.ModelMultipleChoiceField(queryset=Produto.objects.all(), label='Selecionar Produtos', widget=forms.CheckboxSelectMultiple)
    descricao = forms.CharField(label='Descrição')

    def __init__(self, *args, **kwargs):
        super(vendaForm, self).__init__(*args, **kwargs)

        # Adicionar campos de quantidade dinâmicos para cada produto selecionado
        for produto in self.fields['produtos'].queryset:
            self.fields[f'quantidade_{produto.id}'] = forms.IntegerField(
                min_value=0,
                initial=0,
                label=f'Quantidade para {produto.pro_desc}',
                required=False  # O campo não é obrigatório
            )