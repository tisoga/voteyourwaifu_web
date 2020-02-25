from django.shortcuts import render
from .models import test_upload
# Create your views here.
def beranda(request):
    print (test_upload.objects.all()[0].image1)
    if request.method == 'POST':
        if request.POST.get('nama'):
            name = request.POST.get('nama')
            foto1 = request.FILES.get('logo')
            foto1.name = 'logo.png'
            foto2 = request.FILES.get('header')
            foto2.name = 'header.png'
            foto3 = request.FILES.get('body')
            foto3.name = 'body.png'
            test_upload.objects.create(name = name ,image1 = foto1, image2 = foto2, image3 = foto3)
    return render(request = request,
                  template_name = 'html/tambah_series.html')