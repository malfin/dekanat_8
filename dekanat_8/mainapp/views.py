from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from mainapp.models import Group


@login_required
def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


@login_required
def group_list(request):
    group = Group.objects.all()
    context = {
        'title': 'группы',
        'group': group,
    }
    return render(request, 'mainapp/all_group.html', context)
