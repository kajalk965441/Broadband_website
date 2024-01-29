from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    # path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('prices', views.prices, name='prices'),
    path('contact', views.contactlist, name='contact'),
    path('test', views.test, name='test'),
    path('kk', views.kkk, name='kk'),

]