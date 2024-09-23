from django import forms
from .models import Formulario
        
class FormularioContato(forms.ModelForm):
    nome_completo = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nome Completo'})
    )
    telefone = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'Telefone'})
    )
    assunto = forms.ChoiceField(
        label='',
        choices=[
            ('orcamento', 'Orçamentos'),
            ('projeto', 'Projetos'),
            ('servico', 'Serviços'),
            ('duvida', 'Dúvidas'),
            ('outro', 'Outros'),
        ],
        widget=forms.Select(attrs={'placeholder': 'Selecione uma categoria'})
    )

    sobre = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'Descreva sua dúvida ou pedido'})
    )

    class Meta:
        model = Formulario
        fields = ['nome_completo', 'telefone', 'assunto', 'sobre']