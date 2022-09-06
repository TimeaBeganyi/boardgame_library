from django import forms
from django.forms import TextInput, Select, Textarea

from boardgames.models import Boardgame


class BoardgameForm(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ['title', 'publication_year', 'max_players', 'best_players', 'player_age', 'playtime', 'weight',
                  'designer', 'artists', 'language_dependence', 'description', 'types', 'categories', 'mechanics',
                  'available', 'image']

        widgets = {
            'title': TextInput(attrs={'placeholder': 'Please enter the title of the game', 'class': 'form-control'}),
            'publication_year': TextInput(
                attrs={'placeholder': 'Please enter the publication year', 'class': 'form-control'}),
            'max_players': TextInput(
                attrs={'placeholder': 'Please enter the number of players', 'class': 'form-control'}),
            'best_players': TextInput(
                attrs={'placeholder': 'Please enter the best player number', 'class': 'form-control'}),
            'player_age': TextInput(
                attrs={'placeholder': 'Please enter the recommended player age', 'class': 'form-control'}),
            'playtime': TextInput(attrs={'placeholder': 'Please enter the playtime', 'class': 'form-control'}),
            'weight': TextInput(attrs={'placeholder': 'Please enter the weight of the game', 'class': 'form-control'}),
            'designer': TextInput(
                attrs={'placeholder': 'Please enter the designer of the game', 'class': 'form-control'}),
            'artists': TextInput(attrs={'placeholder': 'Please enter the artists', 'class': 'form-control'}),
            'language_dependence': TextInput(
                attrs={'placeholder': 'Please enter the language dependence of the game', 'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'types': Select(attrs={'class': 'form-select'}),
            'categories': Select(attrs={'class': 'form-select'}),
            'mechanics': Select(attrs={'class': 'form-select'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'form-control'
