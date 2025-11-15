from django.db import models

# Create your models here.
class Funcionarios(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    status = models.BooleanField(default=True)
    
    #corrige o problema de duplo 's' no nome do modelo no admin
    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários" # Define o nome plural correto
    def __str__(self):
        return self.nome

class Produtos(models.Model):
    foto = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=80)
    categoria = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    valor = models.FloatField(max_length=20)
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Tipo: {self.descricao}, preço: {self.valor} "
    
class Clientes(models.Model):
    nome= models.CharField(max_length=100)
    idade = models.CharField(max_length=3)
    email = models.EmailField(max_length=100,unique=True)
    contato = models.CharField(max_length=18, blank=True, null=True, unique=True)   
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    # contato/models.py
from django.db import models
from django.utils import timezone

class MensagemContato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.assunto} - {self.nome} ({self.email})"

    class Meta:
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"
        ordering = ['-data_envio'
                    ]

    