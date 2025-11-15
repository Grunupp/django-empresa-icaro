from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Funcionarios, Produtos, Clientes
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import ContatoModelForm , LoginForm , RegistroForm
from django.contrib.messages import constants as message_constants
# Create your views here.


def home(request):
    return render(request,'home.html')

def login_view(request):
    # Se o usuário já estiver autenticado, redireciona para a página inicial.
    if request.user.is_authenticated:
        return redirect('home')

    # Cria uma instância do formulário de login com os dados enviados (se houver).
    form = LoginForm(request.POST or None)

    # Verifica se o método da requisição é POST e se o formulário é válido.
    if request.method == 'POST' and form.is_valid():
        # Autentica o usuário com base nos dados do formulário.
        user = authenticate(
            request,
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )

        # Se a autenticação for bem-sucedida, realiza o login e redireciona para a página inicial.
        if user:
            login(request, user) # Cria e atualiza a sessão do usuário.
            messages.success(request, 'Login Realizado')
            return redirect('home')

        # Caso contrário, exibe uma mensagem de erro.
        messages.error(request, 'Credenciais inválidas')

    # Renderiza o template 'login.html' passando o formulário como contexto.
    return render(request, 'login.html', {'form': form })

# View para registrar um novo usuário.
def registrar_view(request):
    # Se o usuário já estiver autenticado, redireciona para a página inicial.
    if request.user.is_authenticated:
        return redirect('home')

    # Cria uma instância do formulário de registro com os dados enviados (se houver).
    form = RegistroForm(request.POST or None)

    # Verifica se o método da requisição é POST e se o formulário é válido.
    if request.method == 'POST' and form.is_valid():
        # Cria um novo usuário com base nos dados do formulário.
        user = User.objects.create_user(
            username = form.cleaned_data['username'],
            email= form.cleaned_data['email'],
            password= form.cleaned_data['password'],
        )

        # Exibe uma mensagem de sucesso e redireciona para a página de login.
        messages.success(request, 'Conta criada com sucesso.')
        return redirect('login')

    # Renderiza o template 'registrar.html' passando o formulário como contexto.
    return render(request, 'registro.html', {'form': form})

@login_required
def funcionarios(request):
    funcionarios = Funcionarios.objects.filter(status=True)
    context = {'funcionarios': funcionarios}
    return render(request,'funcionarios.html',context)
@login_required
def produtos(request):
    produtos  = Produtos.objects.all()
    context = {'produtos': produtos}
    return render(request,'produtos.html',context)
@login_required
def clientes(request):
    clientes   = Clientes.objects.all()
    context = {'clientes': clientes}
    return render(request,'clientes.html',context)

def logout_view(request):
    # Realiza o logout do usuário, encerrando a sessão.
    logout(request)

    # Exibe uma mensagem informativa e redireciona para a página de login.
    messages.info(request, 'Você saiu')
    return redirect('login')

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
