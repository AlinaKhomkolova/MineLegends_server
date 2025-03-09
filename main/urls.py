from django.urls import path

from main.views import home

urlpatterns = [
    path('', home),
    path('home.html', home, name='home')
]
