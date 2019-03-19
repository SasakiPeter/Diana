from django.shortcuts import render, get_object_or_404, redirect

from .models import Diary
from .form import DiaryForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views import generic


# @login_required
class IndexView(generic.ListView):
    model = Diary
    template_name = 'diaries/index.html'
    paginate_by = 3


def detail(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id)
    return render(request, 'diaries/detail.html', {'diary': diary})


def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm
    return render(request, 'diaries/create.html', {'form': form})


@require_POST
def delete(request, diary_id):
    memo = get_object_or_404(Diary, id=diary_id)
    memo.delete()
    return redirect('diaries:index')
