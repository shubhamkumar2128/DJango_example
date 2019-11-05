from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'kumar'})


def add(request):
    n = int(request.POST['numone'])
    m = int(request.POST['numtwo'])
    result = n + m
    return render(request, 'add.html', {'result': result})
