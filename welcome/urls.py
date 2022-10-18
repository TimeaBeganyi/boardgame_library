from django.urls import path

from welcome import views

urlpatterns= [
    path('', views.WelcomeTemplateView.as_view(), name='welcome'),
    path('about_us/', views.AboutTemplateView.as_view(), name='about'),
    path('faq/', views.FaqTemplateView.as_view(), name='faq'),
    path('index/', views.index, name='index'),

]
