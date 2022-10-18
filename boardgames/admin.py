from django.contrib import admin

from boardgames.models import Boardgame, BoardgameComment, Favourite

admin.site.register(BoardgameComment)
admin.site.register(Favourite)


@admin.register(Boardgame)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "categories")
