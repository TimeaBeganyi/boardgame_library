from django.shortcuts import render
from django.views.generic import TemplateView

import boardgames.models
from boardgames.models import Boardgame, BoardgameInstance
from userextend.models import UserExtend


class WelcomeTemplateView(TemplateView):
    template_name = 'welcome/welcome.html'


class AboutTemplateView(TemplateView):
    template_name = 'welcome/about_us.html'


class FaqTemplateView(TemplateView):
    template_name = 'welcome/faq.html'


def index(request):
    all_games = Boardgame.objects.all().order_by('updated_at').values()

    num_boardgames = Boardgame.objects.all().count()
    num_instances = BoardgameInstance.objects.all().count()
    num_instances_available = BoardgameInstance.objects.filter(status__exact='a').count()
    num_owner = UserExtend.objects.count()

    context = {
        'all_games': all_games,
        'num_boardgames': num_boardgames,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_owner': num_owner,
    }

    return render(request, 'welcome/welcome.html', context=context)
