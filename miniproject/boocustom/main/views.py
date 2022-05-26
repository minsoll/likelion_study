from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def nickname(request):
    return render(request, 'main/nickname.html')
# Create your views here.
