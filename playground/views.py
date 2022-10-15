from django.shortcuts import render


def say_hello(request):
    return render(request, 'playground/hello.html', {'name': 'Ivan'})
