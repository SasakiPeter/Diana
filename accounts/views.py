from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User


def index(request):
    if request.user.is_authenticated:
        user_list = User.objects.all()
        return render(request, 'accounts/index.html', {'user_list': user_list})
    else:
        return redirect('accounts:login')


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'accounts/detail.html'


def login(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # diaries:index
            return redirect('accounts:index')
        else:
            message = "invalid login"
            return render(request, 'accounts/login.html', {'error_message': message})


def logout(request):
    if request.method == "POST":
        auth_logout(request)
    # diaries:index
    return redirect('accounts:index')


def create(request):
    if request.method == "GET":
        return render(request, 'accounts/create.html')

    if request.method == "POST":
        #  Userモデルから、新規ユーザーを作成し、DBに登録する
        # 認証用のメール送ったりしないといけない。
        return redirect('account:index')
