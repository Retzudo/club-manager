from django.shortcuts import render, get_object_or_404

from core.models import Club, Membership


def index(request, slug):
    club = get_object_or_404(Club, slug=slug)

    return render(request, 'clubs/index.html', {
        'club': club,
        'members': Membership.objects.filter(club=club),
        'events': club.events.all(),
        'news': club.news.all(),
        'is_admin': club.user_is_admin(request.user),
    })
