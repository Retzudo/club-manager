from django.shortcuts import render, get_object_or_404

from core.models import Club


def get_club(slug):
    return get_object_or_404(Club, slug=slug)


def is_admin(request, club):
    if request.user.is_authenticated:
        return club.user_is_admin(request.user)
    else:
        return False


def news(request, slug):
    club = get_club(slug)

    return render(request, 'clubs/news.html', {
        'club': club,
        'is_admin': is_admin(request, club),
    })


def events(request, slug):
    club = get_club(slug)

    return render(request, 'clubs/events.html', {
        'club': club,
        'is_admin': is_admin(request, club),
    })


def members(request, slug):
    club = get_club(slug)

    return render(request, 'clubs/members.html', {
        'club': club,
        'is_admin': is_admin(request, club),
    })


def cash(request, slug):
    club = get_club(slug)

    return render(request, 'clubs/cash.html', {
        'club': club,
        'is_admin': is_admin(request, club),
    })


def settings(request, slug):
    club = get_club(slug)

    return render(request, 'clubs/settings.html', {
        'club': club,
        'is_admin': is_admin(request, club),
    })