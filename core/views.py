from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'base.html')


def profile(request):
    return render(request, 'profile.html')
