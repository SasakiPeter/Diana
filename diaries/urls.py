from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
]
