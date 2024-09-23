from django.shortcuts import render,HttpResponse
from .models import Formulario
from .forms import FormularioContato
from django.contrib.messages import constants as message_constants
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def contato(request):
    if request.method == 'POST':
        form = FormularioContato(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.WARNING,
                "Formulário enviado com sucesso, entraremos em contato.",
            )
            
            # Get the cleaned data from the form
            nome_completo = form.cleaned_data['nome_completo']
            telefone = form.cleaned_data['telefone']
            assunto = form.cleaned_data['assunto']
            sobre = form.cleaned_data['sobre']
            
            # Create the email subject and message
            subject = f'Novo contato: {assunto}'  # Include the subject from the form
            message = f'Nome: {nome_completo}\nTelefone: {telefone}\nAssunto: {assunto}\nDetalhes: {sobre}'

            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['pauloaugustocarsten@gmail.com']  # Your email

            # Send the email
            send_mail(subject, message, from_email, recipient_list)

    else:
        form = FormularioContato()

    context = {
        "form": form,
    }
    return render(request, 'contato.html', context)

# Create your views here.
def index(request):
    return render (request, 'index.html')

def sobre(request):
    return render (request, 'sobre.html')

def servicos(request):
    return render (request, 'servicos.html')

def aguas(request):
    return render (request, 'agua.html')

def esgotos(request):
    return render (request, 'esgotos.html')

def accesoria_ambiental(request):
    return render (request, 'accesoria_ambiental.html')

def residuos_solidos(request):
    return render (request, 'residuos_solidos.html')

def test(request):
    forms = FormularioContato()
    context = {
        'forms':forms
    }
    
    return render(request,'test.html',context)
