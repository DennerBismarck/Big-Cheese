from django.db import models

# Create your models here.

class Produto(models.Model):
    pro_desc = models.CharField(max_length = 500, verbose_name = "Descrição do produto")
    pro_preco = models.FloatField(verbose_name = "Preço do produto")

    def __str__(self):
        return self.pro_desc
    
    class Meta:
        verbose_name_plural = "Produtos"

    def save(self, *args, **kwargs):
        self.pro_preco = round(self.pro_preco, 2)
        super(Produto, self).save(*args, **kwargs)

class Venda(models.Model):

    COMPRA_CHOICES = [
        ('Pagou', 'Pagou'),
        ('Não pagou', 'Não Pagou'),
    ]
    ven_pro = models.ManyToManyField(Produto, through='Produtos_Das_Vendas', verbose_name="Produtos da venda")
    ven_precoTotal = models.FloatField(verbose_name="Preço total")
    ven_DataHora = models.DateTimeField(auto_now_add=True, verbose_name = "Data e hora da compra")
    ven_desc = models.CharField(max_length = 1000, verbose_name = "Descrição da venda")
    ven_pago = models.CharField(choices = COMPRA_CHOICES, verbose_name = "Cliente pagou?", max_length = 10, default = 'Não pagou')

    def __str__(self):
        return self.ven_precoTotal
    
    class Meta:
        ordering = ['ven_DataHora']
        verbose_name_plural = "Vendas"  

    def save(self, *args, **kwargs):
        self.ven_precoTotal = round(self.ven_precoTotal, 2)
        super(Venda, self).save(*args, **kwargs)  

class Produtos_Das_Vendas(models.Model):
    pdv_pro = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name = "Código do produto")
    pdv_ven = models.ForeignKey(Venda, on_delete = models.CASCADE, verbose_name = "Código da venda")
    pdv_qtd = models.PositiveIntegerField(default = 0, verbose_name = "Quantidade comprada")
    pdv_PrecoTotalItem = models.FloatField(verbose_name = "Valor total do produto", default = 0.00)

    class Meta:
        verbose_name = "Produtos da venda"
        verbose_name_plural = "Produtos das vendas"

    def save(self, *args, **kwargs):
        self.pdv_PrecoTotalItem = round(self.pdv_PrecoTotalItem, 2)
        super(Produtos_Das_Vendas, self).save(*args, **kwargs)