__author__ = 'Alex'


class Team:
    def __init__(self, name):

        self.name = name
        self.roster = []

    def add_player(self, player):
        self.roster.append(player)

