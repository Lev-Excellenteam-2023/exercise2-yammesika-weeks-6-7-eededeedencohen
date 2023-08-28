#---------------------
# אורטל קומבט - 7.2
#---------------------

import random # for random decrease of health points

class Player:
    """" A class representing a player in a game. 

    :ivar str name: The player's name.
    :ivar int hp: The player's health points.
    :ivar int exp: The player's experience points.
    :ivar int level: The player's level.
    :ivar list nemeses: The player's nemeses.

    :param str name: The player's name.
    :param list nemeses: The player's nemeses.

    :raises ValueError: if the name is empty.
    :raises TypeError: if the nemeses is not a list.
    """
    def __init__(self, name , nemeses):
        if name == "":
            raise ValueError("Name cannot be empty.")
        if not isinstance(nemeses, list):
            raise TypeError("Nemeses must be a list.")
        self.name = name
        self.hp = 100
        self.exp = 0
        self.level = 1
        self.nemeses = nemeses

    def attack(self, player=None):
        """Attack a Player.

        :param Player player: The player to attack. optional.
        :raises ValueError: if there are no nemeses to attack.
        """

        if player is None:
            if len(self.nemeses) == 0:
                raise ValueError("No nemeses to attack.")
            player = self.nemeses[-1]
        player.hp = player.hp - random.randint(self.level*5, self.level*20)

        if player.hp <= 0:
            player.revive()
            player.nemeses.append(self)
            self.gain_exp(player)

    def revive(self):
        """Revive the player."""
        self.hp = 100


    def level_up(self):
        """Level up the player."""
        self.level = self.level + 1


    def gain_exp(self, Player):
        """" Gain experience points from killing a Player.

        :param Player Player: The player to gain experience from.
        """
        self.exp = self.exp + ((Player.level*10) / self.level)
        if self.exp >= 100:
            self.level_up()
            self.exp = self.exp - 100
