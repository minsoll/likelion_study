from django.shortcuts import render, redirect
from users.decorators import login_message_required
from users.models import User
from .forms import CountryWriteForm

def home(request):
    return render(request, 'main/index.html')

#@login_message_required
def select_boo(request):
    return render(request, 'main/select_boo.html')

def select_country(request):
    if request.method == 'POST':
        form = CountryWriteForm(request.POST)
        user = request.user

        if request.POST["send"] == "0":
            country = form.save(commit = False)
            country.nickname = User.objects.get(user_id=user)
            country.country = '인도'
            country.save()
            return render(request, 'main/decorate_boo.html')
            
        elif request.POST["send"] == "1":
            country = form.save(commit = False)
            country.nickname = User.objects.get(user_id=user)
            country.country = '인도네시아'
            country.save()
            return render(request, 'main/decorate_boo.html')
        elif request.POST["send"] == "2":
            country = form.save(commit = False)
            country.nickname = User.objects.get(user_id=user)
            country.country = '일본'
            country.save()
            return render(request, 'main/decorate_boo.html')
        elif request.POST["send"] == "3":
            country = form.save(commit = False)
            country.nickname = User.objects.get(user_id=user)
            country.country = '브라질'
            country.save()
            return render(request, 'main/decorate_boo.html')
        elif request.POST["send"] == "4":
            country = form.save(commit = False)
            country.nickname = User.objects.get(user_id=user)
            country.country = '중국'
            country.save()
            return render(request, 'main/decorate_boo.html')
        elif request.POST["send"] == "5":
            country = form.save(commit = False)
            country.nickname = User.objects.get(user_id=user)
            country.country = '스페인'
            country.save()
            return render(request, 'main/decorate_boo.html')
    return render(request, 'main/select_country.html')

def decorate_boo(request):
    return render(request, 'main/decorate_boo.html')