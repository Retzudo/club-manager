from django.shortcuts import render, get_object_or_404

from core.models import Club


def index(request, slug):
    club = get_object_or_404(Club, slug=slug)

    return render(request, 'clubs/index.html', {
        'club': club,
        'members': club.members.all(),
        'upcoming_events': None,
    })
