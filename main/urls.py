from django.urls import path
from main.views import home, privacy_policy, contact_us


urlpatterns = [
    path('', home, name='home'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('contact/', contact_us, name='contact_us'),
]
