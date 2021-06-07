from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import FormView

from mainapp.forms import GroupForm, StudentForm
from mainapp.models import Group, Student


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


def group_show(request, pk):
    group = get_object_or_404(Group, id=pk)
    students = Student.objects.filter(group=group)
    context = {
        'title': 'группа',
        'students': students,
    }
    return render(request, 'mainapp/group/group_show.html', context)


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


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно добавили студента!')
            return HttpResponseRedirect(reverse('mainapp:group_list'))
    else:
        form = StudentForm()
    context = {
        'title': 'Добавить группу',
        'form': form,
    }
    return render(request, 'mainapp/group/add_group.html', context)


def edit_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили данные о студенте!')
            return HttpResponseRedirect(reverse('mainapp:group_list'))
    else:
        form = StudentForm(instance=student)
    context = {
        'title': 'Изменить данные о студенте',
        'form': form,
    }
    return render(request, 'mainapp/students/add_student.html', context)


def remove_student(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    messages.success(request, 'Вы успешно удалили студента!')
    return HttpResponseRedirect(reverse('mainapp:group_list'))
