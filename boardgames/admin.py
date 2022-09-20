from django.contrib import admin

from boardgames.models import Boardgame, BoardgameComment

admin.site.register(BoardgameComment)


@admin.register(Boardgame)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("title", "categories")
