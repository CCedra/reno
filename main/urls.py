from django.urls import path
from . import views

#Первый атрибут - Имя отображаемое в адресной строке. Второй - Функция на которую мы ссылаемся в вайле views. Третий - имя по которому мы обращаемся в url файлу в программе.
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about-us'),
    path('add', views.add_product, name='add_product'),
]
