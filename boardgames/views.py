from functools import reduce

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView

import boardgames.models
from boardgames.filters import BoardgameFilter
from boardgames.forms import BoardgameForm, BoardgameCommentForm
from boardgames.models import Boardgame, Favourite, BoardgameComment
from userextend.models import UserExtend


class BoardgameCreateView(CreateView):
    template_name = 'boardgames/create_boardgame.html'
    model = Boardgame
    form_class = BoardgameForm
    success_url = reverse_lazy('create-boardgame')
    permission_required = 'boardgame.add_boardgame'


class BoardgameListView(ListView):
    template_name = 'boardgames/list_of_boardgames.html'
    model = Boardgame
    context_object_name = 'all_boardgames'
    permission_required = 'boardgame.view_boardgame'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        category = self.request.GET.get('categories')
        games = self.object_list

        if category:
            games = Boardgame.objects.filter(categories__contains=[category])
        data['all_boardgames'] = games

        my_filter = BoardgameFilter(self.request.GET, queryset=Boardgame.objects.all())
        data['all_boardgames'] = my_filter.qs
        data['my_filter'] = my_filter
        return data


class BoardgameUpdateView(UpdateView):
    template_name = 'boardgames/update_boardgame.html'
    model = Boardgame
    form_class = BoardgameForm
    success_url = reverse_lazy('list-of-boardgames')
    permission_required = 'boardgame.change_boardgame'


class BoardgameDetailView(DetailView):
    template_name = 'boardgames/detail_boardgame.html'
    model = Boardgame
    permission_required = 'boardgame.view_boardgame'

    def get_context_data(self, **kwargs):
        data = super(BoardgameDetailView, self).get_context_data(**kwargs)
        comments = BoardgameComment.objects.filter(title__id=self.kwargs.get('pk'))
        data['comments'] = comments
        rating = 0
        for comment in comments:
            rating += comment.rating
        if comments.count() != 0:
            data['rating'] = rating / comments.count()
        else:
            data['rating'] = rating
        return data


@login_required
@permission_required('boardgame.delete_boardgame')
def delete_boardgame(request, pk):
    Boardgame.objects.filter(id=pk).delete()
    return redirect('list-of-boardgames')


def add_to_fav(request, pk):
    fav = get_object_or_404(Favourite, Boardgame.objects.get(id=pk))
    if fav.favourite.filter(id=request.user.id).exists():
        fav.favourite.remove(request.user)
    else:
        fav.favourite.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def add_to_fav(request, game_id):
#     Favourite.objects.create(user=request.user, game=Boardgame.objects.get(id=game_id))
#     return redirect('list-of-boardgames')


class BoardgameCommentCreateView(CreateView):
    template_name = 'boardgames/create_comment.html'
    model = BoardgameComment
    form_class = BoardgameCommentForm
    success_url = reverse_lazy('list-of-boardgames')
    permission_required = 'boardgame.add_boardgamecomment'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'initial': {'user': self.request.user.id, 'boardgame': self.kwargs.get('pk')}})
        return kwargs


class BoardgameCommentUpdateView(UpdateView):
    template_name = 'boardgames/update_comment.html'
    model = BoardgameComment
    form_class = BoardgameCommentForm
    success_url = reverse_lazy('list-of-boardgames')
    permission_required = 'boardgame.change_boardgame'


@login_required
@permission_required('boardgame.delete_boardgamecomment')
def delete_comment(request, pk):
    BoardgameComment.objects.filter(id=pk).delete()
    return redirect('list-of-boardgames')


def rating(request, game_id):
    rating_number = int(request.POST.get('rating'))
    if 0 <= rating_number <= 5:
        BoardgameComment.objects.create(boardgame=Boardgame.objects.get(id=game_id),
                                        user=UserExtend.objects.get(id=request.user.id), rating=rating_number)
    return redirect('detail-boardgame', pk=game_id)
