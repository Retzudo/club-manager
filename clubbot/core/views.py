from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout as django_logout
from django.contrib.auth import login as django_login


class UserCreationForm(DjangoUserCreationForm):
    class Meta(DjangoUserCreationForm.Meta):
        model = get_user_model()
        fields = ('email',)


def index(request):
    return render(request, 'core/index.html')


def login(request):
    if request.user.is_authenticated:
        return redirect(reverse('account'))

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            django_login(request, form.get_user())
            return redirect(reverse('account'))
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {
        'form': form
    })


def logout(request):
    django_logout(request)
    return redirect(reverse('index'))


@login_required
def account(request):
    return render(request, 'core/account.html')


def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.active = True
            user.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = UserCreationForm()


    return render(request, 'core/register.html', context={
        'form': form
    })
