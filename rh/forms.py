# contato/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import MensagemContato

class ContatoModelForm(forms.ModelForm):
    
    class Meta:
        # 1. Especifica o modelo que este formulário irá usar
        model = MensagemContato
        
        # 2. Especifica os campos do modelo que queremos exibir no formulário.
        #    Note que 'data_envio' e 'lido' não estão aqui, pois
        #    eles são definidos automaticamente (default) e não pelo usuário.
        fields = ['nome', 'email', 'assunto', 'mensagem']

        # 3. (Opcional) Personaliza os widgets para o HTML
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seu-email@exemplo.com', 'class': 'form-control'}),
            'assunto': forms.TextInput(attrs={'placeholder': 'Assunto da mensagem', 'class': 'form-control'}),
            'mensagem': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Digite sua mensagem...', 'class': 'form-control'}),
        }
        
        # 4. (Opcional) Personaliza os labels (rótulos)
        labels = {
            'nome': 'Nome Completo',
            'email': 'Seu E-mail',
        }

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(label="senha", widget=forms.PasswordInput)

class RegistroForm(forms.ModelForm):
    password = forms.CharField(label="senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Comfirme a senha", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','email')
    
    def Clean(self):
        cleaned =super().clean()
        if cleaned.get('senha') != cleaned.get('senha2'):
            raise forms.ValidationError("senhas diferentes")
        return cleaned