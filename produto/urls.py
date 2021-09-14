from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('<slug>', views.DetalheProduto.as_view(), name="detalhe"),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(), name="adicionaraocarrinho"),
    path('remorverdocarrinho/', views.RemoverDoCarrinho.as_view(), name="remorverdocarrinho"),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho"),
    path('finalizar/', views.Finalizer.as_view(), name="finhalizar"),
]