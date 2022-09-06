from django.urls import path

from boardgames import views

urlpatterns = [
    # path('welcome/', views.welcome, name='welcome'),
    path('create_boardgame/', views.BoardgameCreateView.as_view(), name='create-boardgame'),
    path('list_of_boardgames/', views.BoardgameListView.as_view(), name='list-of-boardgames'),
    path('update_boardgame/<int:pk>/', views.BoardgameUpdateView.as_view(), name='update-boardgame'),
    path('detail_boardgame/<int:pk>/', views.BoardgameDetailView.as_view(), name='detail-boardgame'),


]
