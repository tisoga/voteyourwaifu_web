from django.urls import path
from . import views

app_name = 'adminpage'

urlpatterns = [
    path('', views.beranda, name='beranda')
]