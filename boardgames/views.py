from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from boardgames.forms import BoardgameForm
from boardgames.models import Boardgame
from userextend.models import UserExtend


class BoardgameCreateView(CreateView):
    template_name = 'boardgames/create_boardgame.html'
    model = Boardgame
    form_class = BoardgameForm
    success_url = reverse_lazy('create-boardgame')


class BoardgameListView(ListView):
    template_name = 'boardgames/list_of_boardgames.html'
    model = Boardgame
    context_object_name = 'all_boardgames'


class BoardgameUpdateView(UpdateView):
    template_name = 'boardgames/update_boardgame.html'
    model = Boardgame
    form_class = BoardgameForm
    success_url = reverse_lazy('list-of-boardgames')


class BoardgameDetailView(DetailView):
    template_name = 'boardgames/detail_boardgame.html'
    model = Boardgame


# def welcome(request):
#     num_boardgames = Boardgame.objects.all().count()
#     num_instances = BoardgameInstance.objects.all().count()
#     num_instances_available = BoardgameInstance.objects.filter(status__exact='a').count()
#     num_owner = UserExtend.objects.count()
#
#     context = {
#         'num_boardgames': num_boardgames,
#         'num_instances': num_instances,
#         'num_instances_available': num_instances_available,
#         'num_owner': num_owner,
#     }

    # return render(request, 'welcome/welcome.html',context=context)
