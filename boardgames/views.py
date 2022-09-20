from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from boardgames.filters import BoardgameFilter
from boardgames.forms import BoardgameForm, BoardgameCommentForm
from boardgames.models import Boardgame, Favourite, BoardgameComment
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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        category = self.request.GET.get('category')
        games = self.object_list
        if category:
            games = Boardgame.objects.filter(categories__contains=[category])
        data['all_boardgames'] = games
        return data

    def get_context_data_filter(self, **kwargs):
        data_filter = super(BoardgameListView, self).get_context_data(**kwargs)
        my_filter = BoardgameFilter(self.request.GET, queryset=Boardgame.objects.all())
        data_filter['all_boardgames'] = my_filter.qs
        data_filter['my_filter'] = my_filter
        return my_filter


class BoardgameUpdateView(UpdateView):
    template_name = 'boardgames/update_boardgame.html'
    model = Boardgame
    form_class = BoardgameForm
    success_url = reverse_lazy('list-of-boardgames')


class BoardgameDetailView(DetailView):
    template_name = 'boardgames/detail_boardgame.html'
    model = Boardgame


def delete_boardgame(request, pk):
    Boardgame.objects.filter(id=pk).delete()
    return redirect('list-of-boardgames')


def add_to_fav(request, game_id):
    Favourite.objects.create(user=request.user, game=Boardgame.objects.get(id=game_id))
    return redirect('list-of-boardgames')


class BoardgameCommentCreateView(CreateView):
    template_name = 'boardgames/create_comment.html'
    model = BoardgameComment
    form_class = BoardgameCommentForm



