from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.home, name ='main'),
#    path('nickname',views.nickname, name ='nickname'),
    path('select_boo',views.select_boo, name ='select_boo'),
    path('select_country',views.select_country, name ='select_country'),
    path('decorate_boo',views.decorate_boo, name ='decorate_boo'),
    path('saveImage',views.canvasToImage, name ='screenshot'),
]