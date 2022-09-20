from django.urls import path
from userextend import views

urlpatterns = [
    path('create_user/', views.UserExtendCreateView.as_view(), name='create-user'),
    path('my_profile/<int:pk>/', views.UserExtendProfileView.as_view(), name='detail-user'),
    path('update_user/<int:pk>/', views.UserExtendUpdateView.as_view(), name='update-user'),
    path('update_user_profile/<int:pk>/', views.UserExtendUpdateProfileView.as_view(), name='update-user-profile'),
    path('inactive_user/<int:pk>/', views.inactive_user, name='inactive-user'),
    path('active_user/<int:pk>/', views.active_user, name='active-user'),
]
