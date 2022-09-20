from django.shortcuts import render
from django.views.generic import TemplateView

from boardgames.models import Boardgame, BoardgameInstance
from userextend.models import UserExtend


class WelcomeTemplateView(TemplateView):
    template_name = 'welcome/welcome.html'


def index(request):
    all_games = Boardgame.objects.all()
    num_boardgames = Boardgame.objects.all().count()
    num_instances = BoardgameInstance.objects.all().count()
    num_instances_available = BoardgameInstance.objects.filter(status__exact='a').count()
    num_owner = UserExtend.objects.count()

    context = {
        'all_boardgames':all_games,
        'num_boardgames': num_boardgames,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_owner': num_owner,
    }

    return render(request, 'welcome/welcome.html',context=context)

