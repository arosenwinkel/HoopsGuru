# Scouting.py
# Different tools relating to scouting Players

'''

When I scout a player, I should get back a report with the following:
Some Vitals
Overall Grade (A-F)
Grades for {Skill, Athleticism, Intangible, Size, Durability, Potential}
Grades for skill groups based on position
--- Expandable to see how the player ranks in each individual attribute

The CPU cares about:
Some Vitals
Overall Grade
Grades (don't need to be expandable)

So we should be able to request one of two things (for now)
A "data" report (just numbers)
A "written" report (grades + strings for writeups)
Same class, written version just has more information tied to it 

Both compiled using same equations, etc.

'''

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
        self.overall = 0
        self.basic_stats = {}
        self.pos_stats = {}
        self.printed_info = ""

    def print(self):
        print(self.printed_info)


class ProPGReport(ScoutingReport):
    def scout(self, v=False):  # v = verbose, a.k.a. I want string information as well as numbers
        pass

class ProSGReport(ScoutingReport):
    def scout(self, v=False):
        pass


class ProSFReport(ScoutingReport):
    def scout(self, v=False):
        pass


class ProPFReport(ScoutingReport):
    def scout(self, v=False):
        pass


class ProCReport(ScoutingReport):
    def scout(self, v=False):
        pass
