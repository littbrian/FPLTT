from django.contrib import admin
from .models import Club, Player, Team

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name", "logo")   # only fields that exist on Club
    search_fields = ("name",)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "club", "price", "total_points")
    list_filter = ("position", "club")
    search_fields = ("name",)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("user", "name")
    filter_horizontal = ["players"]
