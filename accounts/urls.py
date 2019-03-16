from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<str:username>/', views.detail, name='detail'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
]
