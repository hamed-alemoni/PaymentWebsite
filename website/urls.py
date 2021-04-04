from django.contrib import admin
from django.urls import path
from .views import home,payment

app_name = 'website'

urlpatterns = [
    path('', home,name='home'),
    path('callback', payment,name='payment'),
]