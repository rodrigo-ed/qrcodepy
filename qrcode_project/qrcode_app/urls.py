from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerar_qrcode, name='gerar_qrcode'),
]