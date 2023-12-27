from django.db import models
from django.contrib.auth.models import User
from .games import Game
# Create your models here.

class Player:
    user = models.ForeignKey(User, editable=False)
    nickname = models.CharField(max_length=200,default=user.username)



class Room(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Game, editable=False)
    player1 = models.ForeignKey(Player, editable=False)
    player2 = models.ForeignKey(Player, editable=False)
    player3 = models.ForeignKey(Player, editable=False)
    player4 = models.ForeignKey(Player, editable=False)
    is_done = models.BooleanField(default=False)
    
    