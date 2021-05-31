from django.shortcuts import render


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'mainapp/index.html', context)
