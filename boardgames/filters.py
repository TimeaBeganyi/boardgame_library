import django_filters

from boardgames.models import Boardgame


class BoardgameFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label= 'Title')
    publication_year=django_filters.NumberFilter(field_name='publication_year', lookup_expr='year')
    publication_year__gt=django_filters.NumberFilter(field_name='publication_year', lookup_expr='year__gt')
    publication_year__lt=django_filters.NumberFilter(field_name='publication_year', lookup_expr='year__lt')
    best_players=django_filters.NumberFilter()

    types=django_filters.CharFilter(lookup_expr='icontains', label= 'Type')
    category=django_filters.CharFilter(lookup_expr='icontains', label= 'Category')
    mechanics=django_filters.CharFilter(lookup_expr='icontains', label= 'Mechanics')

    owner=django_filters.CharFilter(lookup_expr='icontains', label= 'User')

    class Meta:
        model=Boardgame
        fields = ['title','available','publication_year','best_players','types','category','mechanics','owner']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.filters['title'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Please enter title'})
        self.filters['available'].field.widget.attrs.update({'class':'form-select'}),
        self.filters['owner'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter owner'})