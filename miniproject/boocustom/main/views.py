from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def nickname(request):
    return render(request, 'main/nickname.html')

def select_boo(request):
    return render(request, 'main/select_boo.html')

def select_country(request):
    return render(request, 'main/select_country.html')

def decorate_boo(request):
    return render(request, 'main/decorate_boo.html')
# Create your views here.
