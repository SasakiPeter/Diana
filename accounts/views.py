from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User


def index(request):
    if request.user.is_authenticated:
        user_list = User.objects.all()
        return render(request, 'accounts/index.html', {'user_list': user_list})
    else:
        return redirect('accounts:signin')


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'accounts/detail.html'


def signin(request):
    if request.method == "GET":
        return render(request, 'accounts/signin.html')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # diaries index
            return redirect('accounts:index')
        else:
            message = "invalid login"
            return render(request, 'accounts/signin.html', {'error_message': message})


def signout(request):
    if request.method == "POST":
        logout(request)
    # diaries:index
    return redirect('accounts:index')


def signup(request):
    if request.method == "GET":
        return render(request, 'accounts/signup.html')

    if request.method == "POST":
        #  Userモデルから、新規ユーザーを作成し、DBに登録する
        # 認証用のメール送ったりしないといけない。
        return redirect('accounts:index')
