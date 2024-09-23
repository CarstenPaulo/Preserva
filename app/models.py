from django.db import models

class Formulario(models.Model):
    ESCOLHAS_ASSUNTO = [
        ('orcamento', 'Orçamento'),
        ('projeto', 'Projeto'),
        ('servico', 'Serviço'),
        ('duvida', 'Dúvida'),
        ('outro', 'Outro'),
    ]
    
    nome_completo = models.CharField(max_length=80)
    telefone = models.CharField(max_length=15, blank=True)
    assunto = models.CharField(max_length=10, choices=ESCOLHAS_ASSUNTO, default='orcamento')
    sobre = models.TextField()