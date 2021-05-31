from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from forms import GroupForm
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


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно добавили группу!')
            return HttpResponseRedirect(reverse('mainapp:group_list'))
    else:
        form = GroupForm()
    context = {
        'title': 'Добавить группу',
        'form': form,
    }
    return render(request, 'mainapp/add_group.html', context)
