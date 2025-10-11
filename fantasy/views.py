from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Team, Player


#Allows user to add players to their team
@login_required
def my_team(request):
    team, created = Team.objects.get_or_create(user=request.user)

    if request.method == "POST":
        if "remove_player" in request.POST:
            player_id = request.POST.get("remove_player")
            team.players.remove(player_id)
        else:
            selected_players = request.POST.getlist("players")
            for player_id in selected_players:
                team.players.add(player_id)
        team.save()
        return redirect("my_team")
    
    players = Player.objects.all()
    return render(request, "fantasy/my_team.html", {
        "team": team,
        "players": players
    })
