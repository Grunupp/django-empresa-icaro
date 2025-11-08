from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('produtos/',views.produtos, name='produtos'),
    path('clientes/',views.clientes, name='clientes'),
    path('funcionarios/',views.funcionarios, name='funcionarios'),
   # A URL para a página do formulário
    # Ex: http://127.0.0.1:8000/contato/
    path('contato/', views.formulario_contato_view, name='contatos'),
    
    # A URL para onde o usuário é enviado após o sucesso
    # Ex: http://127.0.0.1:8000/contato/sucesso/
    path('contato/sucesso/', views.contato_sucesso_view, name='contato_sucesso'),
]
    
