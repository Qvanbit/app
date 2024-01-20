from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Home',
        'content': 'My main page - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_auth': True
    }

    return render(request, 'main/index.html', context=context)


def about(request):
    return HttpResponse('About page')