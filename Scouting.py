# Scouting.py
# Different tools relating to scouting Players

from Player import Player


def scout_pro_primary(this_player):  # takes in a Player object and returns a scouting report for primary position
    if this_player.ps1 == "PG":
        return ProPGReport(this_player)
    elif this_player.ps1 == "SG":
        return ProSGReport(this_player)
    elif this_player.ps1 == "SF":
        return ProSFReport(this_player)
    elif this_player.ps1 == "PF":
        return ProPFReport(this_player)
    elif this_player.ps1 == "C":
        return ProCReport(this_player)
    else:
        print("Tried to scout a player with no position set.")
        return None


class ScoutingReport:
    def __init__(self, this_player):
        self.this_player = this_player

    def print(self):
        pass


class ProPGReport(ScoutingReport):
    def scout(self):
        pass


class ProSGReport(ScoutingReport):
    def scout(self):
        pass


class ProSFReport(ScoutingReport):
    def scout(self):
        pass


class ProPFReport(ScoutingReport):
    def scout(self):
        pass


class ProCReport(ScoutingReport):
    def scout(self):
        pass
