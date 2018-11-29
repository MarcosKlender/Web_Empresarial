from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                'La Caffettiera: Nuevo mensaje de contacto', # Asunto
                'De: {} <{}>\n\nMensaje: \n\n{}'.format(name, email, message), # Cuerpo
                'no-contestar@inbox.mailtrap.io', # Email de Origen
                ['mkcarrascog@pucesd.edu.ec'], # Email de Destino
                reply_to = [email] # Email para Respuesta Inmediata
            )

            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+'?ok')
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fail')

    return render(request, 'contact/contact.html', {'form':contact_form})