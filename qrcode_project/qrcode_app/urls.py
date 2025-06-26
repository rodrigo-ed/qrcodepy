from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerar_qrcode, name='gerar_qrcode'),
    path('download/', views.download_qrcode, name='download_qrcode'),
]