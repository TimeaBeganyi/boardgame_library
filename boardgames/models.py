import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import CASCADE, SET_NULL

from userextend.models import UserExtend

type_choices = (
    ('abstract', 'Abstract'), ('area_control', 'Area Control'), ('campaign/legacy', 'Campaign/Legacy'),
    ('cooperative', 'Cooperative'),
    ('deckbuilder', 'Deckbuilder'), ('dexterity', 'Dexterity'), ('drafting', 'Drafting'),
    ('dungeon_crawler', 'Dungeon-crawler'), ('engine_builder', 'Engine-builder'), ('eurogame', 'Eurogame'),
    ('push_your_luck', 'Push-your-luck'), ('resource_management', 'Resource Management'),
    ('roll_and_move', 'Roll-and-move'),
    ('roll_and_write', 'Roll-and-write'), ('role_playing_game', 'RPG - Role-Playing Game'),
    ('social_deduction', 'Social deduction'), ('storytelling', 'Storytelling'),
    ('worker_placement', 'Worker-placement'),
    ('wargame', 'Wargame')
)
category_choices = (('action', 'Action'), ('adventure', 'Adventure'),
                    ('animals', 'Animals'), ('bluffing', 'Bluffing'), ('card_game', 'Card Game'),
                    ('childrens_game', 'Children"s Game'), ('city_building', 'City Building'),
                    ('civilization', 'Civilization'), ('dice', 'Dice'), ('educational', 'Educational'),
                    ('environmental', 'Environmental'), ('expansion_for_basegame', 'Expention for Base-game'),
                    ('fantasy', 'Fantasy'), ('historical', 'Historical'), ('horror', 'Horror'),
                    ('memory', 'Memory'), ('murder/mystery', 'Murder/Mystery'), ('negotiation', 'Negotiation'),
                    ('party_game', 'Party Game'), ('puzzle', 'Puzzle'), ('science_fiction', 'Science Fiction'),
                    ('sports', 'Sports'), ('strategy', 'Strategy'), ('travel', 'Travel'), ('trivia', 'Trivia'),
                    ('war', 'War'),
                    ('word_game', 'Word Game'), ('zombies', 'Zombies')

                    )

mechanics_choices = (('luck','Luck'),

)


class Boardgame(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    max_players = models.CharField(max_length=30)
    best_players = models.IntegerField()
    playtime = models.CharField(max_length=30)
    player_age = models.CharField(max_length=30)
    weight = models.FloatField()
    designer = models.CharField(max_length=200)
    artists = models.CharField(max_length=200)
    language_dependence = models.CharField(max_length=200)
    description = models.TextField(max_length=500, default=None)

    types = ArrayField(
        models.CharField(choices=type_choices,max_length=200, blank=True, null=True),
    )
    categories = ArrayField(
        models.CharField(choices=category_choices, max_length=200,blank=True, null=True),
    )
    mechanics = ArrayField(
        models.CharField(choices=mechanics_choices, max_length=200,blank=True, null=True), default=list
    )
    owner = models.ForeignKey(UserExtend, on_delete=CASCADE,blank=True, null=True, related_name='boardgames')
    borrower = models.ForeignKey(UserExtend, on_delete=SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.designer}'

#
# class BoardgameInstance(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                           help_text='Unique ID for this particular game across whole library')
#     boardgame = models.ForeignKey('Boardgame', on_delete=models.RESTRICT, null=True)
#     specifics = models.CharField(max_length=200)
#     due_back = models.DateField(null=True, blank=True)
#
#     LOAN_STATUS = (
#         ('o', 'On Loan'),
#         ('a', 'Available'),
#         ('r', 'Reserved'),
#     )
#     status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a',
#                               help_text='Boardgame availability')
#
#     class Meta:
#         ordering = ['due_back']
#
#     def __str__(self):
#         return f'{self.id} ({self.boardgame.title})'
