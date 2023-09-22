from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib import messages as django_messages

def home(request):
    return render(request, 'home.html')


def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        # Save the message as a new Message object
        message = Message(name=name, email=email, message=message_text)
        message.save()

        django_messages.success(request, 'Your message has been saved and sent successfully!')
        return redirect('contact_us')  # Redirect after successful form submission

    return render(request, 'pages/contact_us.html')
