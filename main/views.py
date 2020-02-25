from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.db import IntegrityError
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from .models import SeriesModel, HeroineModel, CustomUser as User, Voted
# Create your views here.

def LoginView(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email = email, password = password)
            if user:
                login(request, user)
                return redirect('main:series')
            else:
                messages.error(request, f'Please Check Your Email or Password')
    return render(request = request,
                 template_name = 'html/login.html')

def register(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            password = request.POST.get('pass')
            pass2 = request.POST.get('pass2')
            if password != pass2:
                messages.error(request, f"Password doesn't match")
                return redirect('main:register')
            email = request.POST.get('email')
            first = request.POST.get('first')
            last = request.POST.get('last')
            try:
                User.object.create_user(email, password, first_name = first, last_name = last)
                messages.success(request, f'Registration Success')
                return redirect('main:login')
            except IntegrityError:
                messages.error(request, f'Email already exists.')
                return redirect('main:register')
    return render(request = request,
                 template_name = 'html/register.html')

def LogoutView(request):
    logout(request)
    return redirect('main:login')

def series(request):
    judul = 'List Series'
    kumpulan_data = SeriesModel.objects.all()
    return render(request = request,
                  template_name = 'html/series.html',
                  context={'kumpulan_data': kumpulan_data, 'judul': judul})

def detail_series(request, id):
    seri = get_object_or_404(SeriesModel, pk = id)
    kumpulan_data = HeroineModel.objects.all().filter(series = seri)
    try:
        is_voted = Voted.objects.get(Q(series = seri) & Q(user = request.user))
        heroine = HeroineModel.objects.get(pk = is_voted.choice)
        is_voted.heroine = heroine.nama
    except:
        is_voted = False
    if request.method == 'POST':
        if request.POST.get('heroine_id'):
            kode = request.POST.get('heroine_id')
            heroine = HeroineModel.objects.get(kode = kode)
            heroine.vote += 1
            heroine.save()
            Voted.objects.create(series = seri, user = request.user, choice = kode)
            messages.success(request, 'Vote Success')
            return redirect('main:detail_series', id)
        else:
            messages.error(request, 'Please Choose Heroine First Before Vote!')
    return render(request = request,
                  template_name = 'html/detail_series.html',
                  context= {'kumpulan_data': kumpulan_data, 'seri': seri, 'is_voted': is_voted})