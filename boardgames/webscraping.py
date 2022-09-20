import bs4
import requests
from django.shortcuts import redirect

from boardgames.models import Boardgame


def get_data_gbb(request):
    url = 'https://boardgamegeek.com/boardgame/174430/gloomhaven'
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    cases = soup.find_all('div', class_='game-header-body')
    all_games = {'data': []}

    for case in cases:
        data={}

        title = case.find('div', class_='game-header-title-info')


        if title is None:
            data['title']='No data available'
        else:
            data['title']=title



        all_games['data'].append(data)

    for game in all_games['data']:
        Boardgame.objects.create(title=game.get('title'),
                                 publication_year=2022,
                                 max_players=' ',
                                 best_players=2,
                                 player_age=' ',
                                 playtime=' ',
                                 weight=3,
                                 designer=' ',
                                 artists=' ',
                                 language_dependence=' ',
                                 description=' ',
                                 types=' ',
                                 categories=' ',
                                 mechanics=' ',

                                 )
    return redirect('welcome')


