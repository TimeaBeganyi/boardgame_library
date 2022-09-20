from django.urls import path

from boardgames import views, webscraping

urlpatterns = [
    # path('welcome/', views.welcome, name='welcome'),
    path('create_boardgame/', views.BoardgameCreateView.as_view(), name='create-boardgame'),
    path('list_of_boardgames/', views.BoardgameListView.as_view(), name='list-of-boardgames'),
    path('update_boardgame/<int:pk>/', views.BoardgameUpdateView.as_view(), name='update-boardgame'),
    path('detail_boardgame/<int:pk>/', views.BoardgameDetailView.as_view(), name='detail-boardgame'),
    path('create_comment/', views.BoardgameCommentCreateView.as_view(), name='create-comment'),
    path('delete_boardgame/<int:pk>/', views.delete_boardgame, name='delete-boardgame'),
    path('list_of_games_bgg/', webscraping.get_data_gbb, name='list-of-games-bgg'),
    path('game/<int:game_id>/add_to_fav/', views.add_to_fav, name='add-to-fav'),


]
