from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from core.forms import UserProfileForm
from core.models import UserProfile


def index(request):
    return render(request, 'core/index.html')


def dashboard(request):
    return render(request, 'base.html')


@login_required
def profile(request):
    user = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form = UserProfileForm(instance=user)

    context = {
        'user': user,
        'form': form,
    }

    return render(request, 'core/profile.html', context=context)
