import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE, SET_NULL
from django.urls import reverse
from django_jsonform.models.fields import ArrayField

from userextend.models import UserExtend

type_choices = (
    ('Abstract', 'abstract'), ('Area Control', 'area_control'), ('Campaign/Legacy', 'campaign/legacy'),
    ('Cooperative', 'cooperative'), ('Deckbuilder', 'deckbuilder'), ('Dexterity', 'dexterity'),
    ('Drafting', 'drafting'), ('Dungeon Crawler', 'dungeon_crawler'), ('Engine Builder', 'engine_builder'),
    ('Eurogame', 'eurogame'), ('Family', 'family'), ('Push your luck', 'push-your-luck'),
    ('Resource Management', 'resource_management'),
    ('Roll-and-move', 'roll_and_move'), ('Roll-and-write', 'roll_and_write'), ('Family', 'family'),
    ('RPG - Role-Playing Game', 'role_playing_game'), ('Social deduction', 'social_deduction'),
    ('Strategy', 'strategy'), ('Party', 'party'),
    ('Storytelling', 'storytelling'), ('Worker-placement', 'worker_placement'), ('Wargame', 'wargame')
)
category_choices = (('Action', 'action'), ('Adventure', 'adventure'), ('Abstract Strategy', 'abstract_strategy'),
                    ('Animals', 'animals'), ('Bluffing', 'bluffing'), ('Card Game', 'card_game'),
                    ('Children"s Game', 'childrens_game'), ('City Building', 'city_building'),
                    ('Civilization', 'civilization'), ('Dice', 'dice'), ('Educational', 'educational'),
                    ('Environmental', 'environmental'), ('Expansion for Base-game', 'expansion_for_basegame'),
                    ('Fantasy', 'fantasy'), ('Historical', 'historical'), ('Horror', 'horror'),
                    ('Memory', 'memory'), ('Murder/Mystery', 'murder/mystery'), ('Negotiation', 'negotiation'),
                    ('Party Game', 'party_game'), ('Puzzle', 'puzzle'), ('Science Fiction', 'science_fiction'),
                    ('Sports', 'sports'), ('Strategy', 'strategy'), ('Travel', 'travel'), ('Trivia', 'trivia'),
                    ('War', 'war'), ('Word Game', 'word_game'), ('Zombies', 'zombies')
                    )
mechanics_choices = (
    ('Action Drafting', 'action_drafting'), ('Action Points', 'action_points'), ('Action_timer', 'Action Timer'),
    ('Alliances', 'alliances'), ('Aria Majority', 'area_majority'), ('Area Movement', 'area_movement'),
    ('Area Control', 'area_control'), ('Card Drafting', 'card_drafting'), ('Hand Management', 'hand_management'),
    ('Auction/Bidding', 'auction_bidding'), ('Betting and Bluffing', 'betting_bluffing'),
    ('Campaign/Battle Card Driven', 'campaign_battle_card_driven'), ('Open Drafting', 'open_drafting'),
    ('Closed Drafting', 'closed_drafting'), ('Cooperative Game', 'cooperative_game'),
    ('Deck construction', 'deck_construction'), ('Dice Rolling', 'dice_rolling'), ('Drawing', 'drawing'),
    ('Grid Movement', 'grid_movement'), ('Hand Management', 'hand_management'), ('Hidden Roles', 'hidden_roles'),
    ('Hot Potato', 'hot_potato'), ('I cut you Choose', 'i_cut_you_choose'), ('Investment', 'investment'),
    ('Ladder Climbing', 'ladder_climbing'), ('Layering', 'layering'), ('Legacy game', 'legacy_game'),
    ('Pattern Recognition', 'pattern_recognition'), ('Pattern Building', 'pattern_building'),
    ('Pick-up nad Deliver', 'pick_up_and_deliver'), ('Square Grid', 'square_grid'),
    ('Player Elimination', 'player_elimination'), ('Point-to-Point Movement', 'point2point_movement'),
    ('Push Your Luck', 'push_your_luck'), ('Real Time', 'real_time'), ('Route Building', 'route_building'),
    ('Set Collecting', 'set_collecting'), ('Story Telling', 'story_telling'), ('Social Deduction', 'social_deduction'),
    ('Take that', 'take_that'), ('Tile Placement', 'tile_placement'), ('Worker Placement', 'worker_placement'),
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
    description = models.TextField(max_length=1000, default=None)

    types = ArrayField(
        models.CharField(choices=type_choices, max_length=200, blank=True, null=True),
    )
    categories = ArrayField(
        models.CharField(choices=category_choices, max_length=200, blank=True, null=True),
    )
    mechanics = ArrayField(
        models.CharField(choices=mechanics_choices, max_length=200, blank=True, null=True), default=list
    )
    owner = models.ForeignKey(UserExtend, on_delete=CASCADE, blank=True, null=True, related_name='boardgames')
    borrower = models.ForeignKey(UserExtend, on_delete=SET_NULL, blank=True, null=True)

    image = models.ImageField(upload_to='images/', blank=True, null=True)

    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'{self.title}'


class Favourite(models.Model):
    user = models.ForeignKey(UserExtend, on_delete=SET_NULL, blank=True, null=True)
    game = models.ForeignKey(Boardgame, on_delete=SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.game.title}'


RATING_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))


class BoardgameComment(models.Model):
    title = models.ForeignKey(Boardgame, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(UserExtend, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=300, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('detail-boardgame', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}: {self.comment}'


class BoardgameInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular game across whole library')
    boardgame = models.ForeignKey('Boardgame', on_delete=models.RESTRICT, null=True)
    specifics = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a',
                              help_text='Boardgame availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.boardgame.title})'
