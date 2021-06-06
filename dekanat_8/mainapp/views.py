from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import FormView

from mainapp.forms import GroupForm
from mainapp.models import Group


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)


def group_list(request):
    groups = Group.objects.all()
    context = {
        'title': 'группы',
        'groups': groups,
    }
    return render(request, 'mainapp/group/all_group.html', context)


# class CreateGroupViews(FormView):
#     template_name = 'mainapp/group/all_group.html'
#     form_class = GroupForm
#     success_url = HttpResponseRedirect(reverse('mainapp:group_list'))
#
#     def form_valid(self, form):
#         form.save()
#         return HttpResponseRedirect(reverse('mainapp:group_list'))


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
    return render(request, 'mainapp/group/add_group.html', context)


def edit_group(request, pk):
    group = get_object_or_404(Group, id=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили группу!')
            return HttpResponseRedirect(reverse('mainapp:group_list'))
    else:
        form = GroupForm(instance=group)
    context = {
        'title': 'Изменить группу',
        'form': form,
    }
    return render(request, 'mainapp/group/add_group.html', context)


def remove_group(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()
    messages.success(request, 'Вы успешно удалили группу!')
    return HttpResponseRedirect(reverse('mainapp:group_list'))
