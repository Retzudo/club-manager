from django.shortcuts import render, get_object_or_404

from core.models import Club


def index(request, slug):
    club = get_object_or_404(Club, slug=slug)

    if request.user.is_authenticated:
        is_admin = club.user_is_admin(request.user)
    else:
        is_admin = False

    return render(request, 'clubs/index.html', {
        'club': club,
        'is_admin': is_admin,
    })
