from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
# from django.views import generic
# from django.views.decorators.http import require_POST
from .models import Diary
from .form import DiaryForm

User = get_user_model()


# class IndexView(LoginRequiredMixin, generic.ListView):
#     model = Diary
#     template_name = 'diaries/index.html'
#     paginate_by = 3

def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj


PAGE_PER_ITEM = 1


@login_required()
def index(request):
    diary_list = Diary.objects.filter(user=request.user)
    page_obj = paginate_query(request, diary_list, PAGE_PER_ITEM)

    contexts = {
        'diary_list': diary_list,
        'user': request.user,
        'page_obj': page_obj
    }

    return render(request, 'diaries/index.html', contexts)


@login_required
def detail(request, diary_id):
    diary = get_object_or_404(Diary, id=diary_id)
    return render(request, 'diaries/detail.html', {'diary': diary})


@login_required
def create(request):
    form = DiaryForm(request.POST or None)
    if request.method == 'POST':
        # form = DiaryForm(request.POST)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.user = request.user
            diary.save()
            return redirect('diaries:index')
    # else:
    # form = DiaryForm
    return render(request, 'diaries/create.html', {'form': form})


@login_required
def delete(request, diary_id):
    if request.method == 'POST':
        memo = get_object_or_404(Diary, id=diary_id)
        memo.delete()
    return redirect('diaries:index')
