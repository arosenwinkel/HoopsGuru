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
Skill Grades (don't need to be expandable)

So we should be able to request one of two things (for now)
A "data" report (just numbers)
A "written" report (grades + strings for writeups)
Same class, written version just has more information tied to it 

Both compiled using same equations, etc.

'''

from Player import Player

def repr_length(n):  # represent a given length (inches) in feet plus inches
    feet = n // 12
    inches = n % 12
    return '''{}'{}"'''.format(feet, inches)

def repr_pos(pos):
    if pos == 0:
        print("Invalid pos.")
        return None
    elif pos == 1:
        return "PG"
    elif pos == 2:
        return "SG"
    elif pos == 3:
        return "SF"
    elif pos == 4:
        return "PF"
    elif pos == 5:
        return "C"

def letter_grade(n):
    if n > 100 or n < 0:
        print ("Invalid input for letter_grade:", n)
    if n > 90:
        return "A+"
    elif n > 85:
        return "A"
    elif n > 80:
        return "A-"
    elif n > 75:
        return "B+"
    elif n > 70:
        return "B"
    elif n > 65:
        return "B-"
    elif n > 60:
        return "C+"
    elif n > 50:
        return "C"
    elif n > 45:
        return "C-"
    elif n > 40:
        return "D+"
    elif n > 35:
        return "D"
    elif n > 30:
        return "D-"
    else:
        return "F"

def gfr(n, floor, ceiling, weight):
    if n < floor:
        return 0
    if n > ceiling:
        return weight
    return (( n - floor ) / float( ceiling - floor )) * weight


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


class Aggregate:
    def __init__(self, name):
        self.skill_reports = []
        self.agg_report = ""
        self.name = name
        self.agg_grade = -1
        self.entropy = -1

    def grade(self, n):
        self.agg_grade = n
        self.entropy = abs(n - 50)

    def add_skill(self, s):
        self.skill_reports.append(s)

    def print(self):
        print( "{}... {}".format(self.name, letter_grade(self.agg_grade) ) )
        print( self.agg_report )
        for r in self.skill_reports:  # print each skill, indented
            print("   -", r)


class ScoutingReport:
    def __init__(self, this_player):
        self.this_player = this_player
        self.overall = 0
        self.basic_stats = {}
        self.aggs = []

    def print(self):
        print("--- {} {} ---".format(self.this_player.fnm, self.this_player.lnm))
        print("ID:", self.this_player.id)
        if self.this_player.ps2 != 0:
            print("{}/{}".format(repr_pos(self.this_player.ps1), repr_pos(self.this_player.ps2)))
        else:
            print(repr_pos(self.this_player.ps1))
        print("Height: {}, Wingspan: {}, Weight: {}".format(self.this_player.hgt, self.this_player.wng, self.this_player.wgt))

        self.aggs = sorted(self.aggs, key=lambda a: a.entropy, reverse=True)  # sort by entropy of grades
        for a in self.aggs:
            a.print()


class ProPGReport(ScoutingReport):
    def scout(self, v=False):  # v = verbose, a.k.a. I want string information as well as numbers
        ''' SIZE AGGREGATE '''
        size_agg = Aggregate("Size")
        size_grade = 0
        height = self.this_player.hgt
        size_grade += gfr( height, 70, 78, 100)
        if height < 70:
            size_agg.add_skill("Short for his position at {}".format(repr_length(height)))
        elif height < 73:
            size_agg.add_skill("A little on the short side at {}".format(repr_length(height)))
        elif height < 76:   
            size_agg.add_skill("Solid height at {}".format(repr_length(height)))
        elif height < 78:
            size_agg.add_skill("Excellent height at {}".format(repr_length(height)))
        else:
            size_agg.add_skill("Rare height for his position at {}".format(repr_length(height)))

        ws = self.this_player.wng
        size_grade += gfr( ws, 72, 84, 100)
        if ws < 72:
            size_agg.add_skill("Short arms at {}".format(repr_length(ws)))
        elif ws < 76:
            size_agg.add_skill("Good length for his position at {}".format(repr_length(ws)))
        elif ws < 80:
            size_agg.add_skill("Impressive wingspan at {}".format(repr_length(ws)))
        elif ws < 84:
            size_agg.add_skill("Exceptional length at {}".format(repr_length(ws)))
        else:
            size_agg.add_skill("Freakish wingspan at {}".format(repr_length(ws)))

        if size_grade < 25:
            size_agg.agg_report = "Size really hurts him at this level."
        elif size_grade < 50:
            size_agg.agg_report = "Below average size."
        elif size_grade < 75:
            size_agg.agg_report = "Good size."
        else:
            size_agg.agg_report = "Elite size for his position."

        size_agg.grade(size_grade)
        self.aggs.append(size_agg)

        ''' ATHLETICISM AGGREGATE '''
        ''' SHOOTING AGGREGATE '''
        ''' ATTACKING AGGREGATE '''
        ''' PLAYMAKING AGGREGATE '''
        ''' PERIMETER DEFENSE AGGREGATE '''
        ''' REBOUNDING AGGREGATE '''
        ''' MENTAL AGGREGATE '''
        ''' DURABILITY AGGREGATE '''

        # Grade basic stats last: Technique, Intangible, Physical, Potential
        

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
