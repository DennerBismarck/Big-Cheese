from django.contrib import admin
from API import models
# Register your models here.

admin.site.register(models.Produto)
admin.site.register(models.Produtos_Das_Vendas)
admin.site.register(models.Venda)