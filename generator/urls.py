from django.urls import path
from .views import home, password, passwordRecord, showPasswords, deletePasswords, about

urlpatterns = [
    path('', home, name='home'),
    path('password', password, name='password'),
    path('password/passwordRecord/', passwordRecord, name='passwordRecord'),
    path('saves', showPasswords, name='saves'),
    path('about', about, name='about'),
    path('delete/<int:id>', deletePasswords, name='delete'),
]