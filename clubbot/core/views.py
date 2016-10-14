from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = get_user_model()
        fields = ('email',)


def index(request):
    return render(request, 'core/index.html', {
        'clubs': request.user.clubs.all()
    })


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = UserCreationForm()


    return render(request, 'core/register.html', context={
        'form': form
    })
