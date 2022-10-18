import django_filters
from django_filters import filters

from boardgames.models import Boardgame

class CharArrayFilter(filters.BaseCSVFilter, filters.CharFilter):
    pass


class BoardgameFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label= 'Title')
    publication_year=django_filters.NumberFilter()
    publication_year_gt=django_filters.NumberFilter(field_name='publication_year', lookup_expr='gte')
    publication_year_lt=django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte')
    best_players=django_filters.NumberFilter()

    types=CharArrayFilter(lookup_expr='contains', label= 'Type')
    categories=CharArrayFilter(lookup_expr='contains', label= 'Category')
    mechanics=CharArrayFilter(lookup_expr='contains', label= 'Mechanics')



    class Meta:
        model=Boardgame
        fields = ['title','available','publication_year','best_players','types','categories','mechanics','owner']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.filters['title'].field.widget.attrs.update({'class':'form-control', 'placeholder':'Please enter title'})
        self.filters['available'].field.widget.attrs.update({'class':'form-select'}),
        self.filters['owner'].field.widget.attrs.update({'class': 'form-select'})
        self.filters['types'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['categories'].field.widget.attrs.update({'class': 'form-control'})
        self.filters['mechanics'].field.widget.attrs.update({'class': 'form-control'})