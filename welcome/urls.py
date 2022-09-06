from django.urls import path

from welcome import views

urlpatterns = [
    path('', views.WelcomeTemplateView.as_view(), name='welcome')
]
