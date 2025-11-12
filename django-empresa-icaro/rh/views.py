from django.shortcuts import redirect, render
from .models import Funcionarios, Produtos, Clientes
from .forms import ContatoModelForm
# Create your views here.
def home(request):
    return render(request,'home.html')

def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {'funcionarios': funcionarios}
    return render(request,'funcionarios.html',context)

def produtos(request):
    produtos  = Produtos.objects.all()
    context = {'produtos': produtos}
    return render(request,'produtos.html',context)

def clientes(request):
    clientes   = Clientes.objects.all()
    context = {'clientes': clientes}
    return render(request,'clientes.html',context)

# A view principal do formulário
def formulario_contato_view(request):
    if request.method == 'POST':
        # Cria a instância do formulário com os dados vindos do request
        form = ContatoModelForm(request.POST)
        
        if form.is_valid():
            # A MÁGICA DO MODELFORM:
            # form.save() cria e salva um novo objeto 'MensagemContato'
            # no banco de dados com os dados do formulário.
            form.save()
            
            # Redireciona para uma página de sucesso
            return redirect('contato_sucesso')
    
    else:
        # Se for um GET, apenas cria um formulário vazio
        form = ContatoModelForm()

    # Passa o formulário (vazio ou com erros) para o template
    return render(request, 'contato/contatos.html', {'form': form})


# Uma view simples para a página de "sucesso"
def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')
