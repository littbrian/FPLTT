from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


#creating clubs
class Club(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name =models.CharField(max_length=10, blank=True)
    logo = models.ImageField(upload_to="club_logos/", blank=True, null=True)

    def __str__(self):
        return self.name
    

# Player Model
class Player(models.Model):
    POSITIONS = [
        ("GK","GoalKeeper"),
        ("DEF", "Defender"),
        ("MID", "Midfielder"),
        ("FWD", "Foward")
    ]

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=3, choices=POSITIONS)
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name="players")
    price = models.DecimalField(max_digits=5, decimal_places=2, default=4.0)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.position}) "


# Picking a team
class Team(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="fantasy_team")
    name = models.CharField(max_length=100, default="My Team")
    players = models.ManyToManyField("Player", blank=True)

    def __str_(self):
        return f"{self.user.username}'s Team"
