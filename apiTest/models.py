from django.db import models

# Create your models here.

class Player(models.Model):
    player1Hp = models.IntegerField(default=100)
    player2Hp = models.IntegerField(default=100)

    def __str__(self):
        return {self.player1Hp, self.player2Hp}

