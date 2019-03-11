from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<str:username>/', views.detail, name='detail'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
]
