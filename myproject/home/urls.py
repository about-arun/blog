from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('recent/', views.recent, name="recent"),
    path('add/', views.add, name="add"),
    path('insert', views.insert, name='insert'),
    path('find/<id>', views.find, name='find'),
    

   
]

