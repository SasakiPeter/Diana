from django.shortcuts import render


def index(request):
    return render(request, 'diaries/index.html')


def detail(request):
    return render(request, 'diaries/detail.html')


def create(request):
    return render(request, 'diaries/create.html')
