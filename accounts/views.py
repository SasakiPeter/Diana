from django.conf import settings
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.views import generic
from logging import getLogger
from .forms import LoginForm, SignUpForm
from .models import User

logger = getLogger(__name__)


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
    login_form = LoginForm(request.POST or None)

    if request.method == "GET":
        if request.user.is_authenticated:
            # diaries:index
            return redirect('accounts:index')
        else:
            return render(request, 'accounts/signin.html', {'form': login_form})

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
            return render(request, 'accounts/signin.html', {'form': login_form, 'error_message': message})


def signout(request):
    if request.method == "POST":
        logout(request)
    # diaries:index
    return redirect('accounts:index')


def signup(request):
    signup_form = SignUpForm(request.POST or None)

    if request.method == "GET":
        if request.user.is_authenticated:
            # diaries:index
            return redirect('accounts:index')
        else:
            return render(request, 'accounts/signup.html', {'form': signup_form})

    if request.method == "POST" and signup_form.is_valid():
        user = signup_form.save(commit=False)
        user.display_name = user.username
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        domain = current_site.domain
        context = {
            'user': user,
            'protocol': request.scheme,
            'domain': domain,
            'token': dumps(user.pk)
        }

        subject_template = get_template(
            'accounts/mail_template/signup/subject.txt')
        subject = subject_template.render()

        message_template = get_template(
            'accounts/mail_template/signup/message.txt')
        message = message_template.render(context)

        user.email_user(subject, message)
        return redirect('accounts:signup_done')
    else:
        return render(request, 'accounts/signup.html', {'form': signup_form})


def signup_done(request):
    return render(request, 'accounts/signup_done.html')


def signup_complete(request, token):
    timeout_secs = getattr(settings, 'ACTIVATION_TIMEOUT_SECONDS', 60*60*24)
    if request.method == "GET":
        try:
            user_pk = loads(token, max_age=timeout_secs)
        except SignatureExpired:
            return HttpResponseBadRequest()
        except BadSignature:
            return HttpResponseBadRequest()
        else:
            try:
                user = User.objects.get(pk=user_pk)
            except User.DoesNotExist:
                return HttpResponseBadRequest()
            else:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    login(request, user)
                    # diaries index
                    return redirect('accounts:index')

    return HttpResponseBadRequest()
