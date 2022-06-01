from django.shortcuts import render


def home(request):
    return render(request, 'choose_dress/index.html')
