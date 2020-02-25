from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.series, name='series'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('register/', views.register, name='register'),
    path('series/<int:id>/', views.detail_series, name='detail_series')
]