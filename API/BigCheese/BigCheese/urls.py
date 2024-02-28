"""
URL configuration for BigCheese project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path('admin/', admin.site.urls),

#URL da página inicial
    path('', views.index, name="index"),

    path('Produtos/', views.TabelaProdutos, name="tabelaProdutos"),
    path('editarProduto/<int:id>', views.editarProduto, name="editarproduto"),
    path('deletarProduto/<int:id>', views.deletarProduto,name="deletarproduto"),

    path('Vendas/', views.cadastrarVenda, name="tabelaVendas"),
    path('editarVenda/<int:id>',views.editarvenda, name="editarvenda"),
    path('deletarVenda/<int:id>', views.deletarvenda, name="deletarvenda")
]
