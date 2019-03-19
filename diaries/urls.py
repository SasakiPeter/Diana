from django.urls import path
from . import views

app_name = 'diaries'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:diary_id>/', views.delete, name='delete'),
    path('detail/<int:diary_id>/', views.detail, name='detail')
]
