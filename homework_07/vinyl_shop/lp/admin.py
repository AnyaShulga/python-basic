from django.contrib import admin

from .models import Lp, LpGenre, RecordLabel

@admin.register(RecordLabel)
class RecordLabelAdmin(admin.ModelAdmin):
    list_display = "pk", "name"
    list_display_links = "pk", "name"

@admin.register(Lp)
class LpAdmin(admin.ModelAdmin):
    list_display = "pk", "artist", "album", "year", "condition"
    list_display_links = "pk", "artist", "album"
    ordering = "artist", "album"

@admin.register(LpGenre)
class LpGenreAdmin(admin.ModelAdmin):
    list_display = "pk", "genre"
    list_display_links = "pk", "genre"