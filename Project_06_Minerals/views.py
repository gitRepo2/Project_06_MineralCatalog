from django.shortcuts import render


def index(request):
    return render(request, 'minerals_app/index.html')