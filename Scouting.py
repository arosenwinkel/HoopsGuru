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
        print("{} years old".format(self.this_player.age))
        if self.this_player.ps2 != "None":
            print("{}/{}".format(self.this_player.ps1, self.this_player.ps2))
        else:
            print(self.this_player.ps1)
        print("Height: {}, Wingspan: {}, Weight: {} lbs.".format(repr_length(self.this_player.hgt), 
            repr_length(self.this_player.wng), self.this_player.wgt))

        self.aggs = sorted(self.aggs, key=lambda a: a.entropy, reverse=True)  # sort by entropy of grades
        for a in self.aggs:
            a.print()

        print()


class ProPGReport(ScoutingReport):
    def scout(self, v=False):  # v = verbose, a.k.a. I want string information as well as numbers
        ''' SIZE AGGREGATE '''
        size_agg = Aggregate("Size")
        size_grade = 0
        height = self.this_player.hgt
        size_grade += gfr( height, 70, 78, 50)
        if height < 71:
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
        size_grade += gfr( ws, 72, 84, 50)
        if ws < 72:
            size_agg.add_skill("Poor length for his position.")
        elif ws < 76:
            size_agg.add_skill("Good length for his position.")
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
        ath_agg = Aggregate("Athleticism")
        ath_grade = 0

        quickness = self.this_player.ath["qui"]
        ath_grade += gfr( quickness, 50, 95, 20 )
        if quickness < 50:
            ath_agg.add_skill("No explosiveness to speak of.")
        elif quickness < 75:
            ath_agg.add_skill("Not exceptionally explosive.")
        elif quickness < 85:
            ath_agg.add_skill("Good explosivess.")
        else:
            ath_agg.add_skill("Incredibly explosive.")

        vertical = self.this_player.ath["vrt"]
        ath_grade += gfr( vertical, 30, 95, 20 )
        if vertical < 30:
            ath_agg.add_skill("No leaping ability to speak of.")
        elif vertical < 50:
            ath_agg.add_skill("Limited leaping ability.")
        elif vertical < 75:
            ath_agg.add_skill("Average leaping ability.")
        elif vertical < 85:
            ath_agg.add_skill("Great leaping ability.")
        else:
            ath_agg.add_skill("Otherworldly leaping ability.")

        strength = self.this_player.ath["str"]
        ath_grade += gfr( strength, 10, 50, 20 )
        if strength < 20:
            ath_agg.add_skill("Very little upper-body strength.")
        elif strength < 30:
            ath_agg.add_skill("Acceptable upper-body strength.")
        elif strength < 40:
            ath_agg.add_skill("Good upper-body strength.")
        else:
            ath_agg.add_skill("Great upper-body strength.")

        speed = self.this_player.ath["spd"]
        ath_grade += gfr( speed, 50, 95, 20 )
        if speed < 50:
            ath_agg.add_skill("Too slow on the open floor.")
        elif speed < 75:
            ath_agg.add_skill("Average speed on the open floor.")
        elif speed < 85:
            ath_agg.add_skill("Good speed on the open floor.")
        else:
            ath_agg.add_skill("Excellent speed on the open floor.")

        nat_fit = self.this_player.ath["fit"]
        ath_grade += gfr( nat_fit, 50, 95, 20 )
        if nat_fit < 50:
            ath_agg.add_skill("Very poor conditioning.")
        elif nat_fit < 75:
            ath_agg.add_skill("Conditioning is suspect at times.")

        if ath_grade < 25:
            ath_agg.agg_report = "Poor athletic ability for his position."
        elif ath_grade < 50:
            ath_agg.agg_report = "Below average athletic ability."
        elif ath_grade < 75:
            ath_agg.agg_report = "Good athletic ability."
        else:
            ath_agg.agg_report = "Exceptional athletic ability."

        ath_agg.grade(ath_grade)
        self.aggs.append(ath_agg)

        ''' SHOOTING AGGREGATE '''
        # Height, range, off-ball, consistency
        shoot_agg = Aggregate("Shooting")
        shoot_grade = 0

        shoot_grade += gfr( height, 70, 78, 10)
        if height < 73:
            shoot_agg.add_skill("Has difficulty getting his shot off against taller players.")
        elif height > 75:
            shoot_agg.add_skill("No trouble getting his shot off over defenders.")

        rng = self.this_player.fun["rng"]
        shoot_grade += gfr( rng, 20, 95, 50 )
        if rng < 20:
            shoot_agg.add_skill("Shooting range is very much a work in progress.")
        elif rng < 40:
            shoot_agg.add_skill("Range extends out to midrange.")
        elif rng < 60:
            shoot_agg.add_skill("Range extends out to the 3-point line.")
        elif rng < 80:
            shoot_agg.add_skill("Reliable from deep.")
        else:
            shoot_agg.add_skill("Easily knocks down shots from beyond the 3-point line.")

        off_ball = self.this_player.iq["obl"]
        shoot_grade += gfr( off_ball, 20, 95, 20 )
        if off_ball < 20:
            shoot_agg.add_skill("Looks completely lost when the ball is out of his hands.")
        elif off_ball < 40:
            shoot_agg.add_skill("Hesitant when the ball is out of this hands.")
        elif off_ball < 60:
            shoot_agg.add_skill("Works well off the ball.")
        elif off_ball < 80:
            shoot_agg.add_skill("Works to get himself open off the ball.")
        else:
            shoot_agg.add_skill("Easily finds open floor when the ball is out of his hands.")

        consistency = self.this_player.men["cns"]
        shoot_grade += gfr( consistency, 20, 95, 20 )
        if consistency < 25:
            shoot_agg.add_skill("Not consistent.")
        elif consistency < 50:
            shoot_agg.add_skill("Too streaky to be a reliable option.")
        elif consistency > 74:
            shoot_agg.add_skill("Very consistent player.")

        if shoot_grade < 25:
            shoot_agg.agg_report = "Ineffective as a jump shooter."
        elif shoot_grade < 50:
            shoot_agg.agg_report = "Can make jump shots in a pinch."
        elif shoot_grade < 75:
            shoot_agg.agg_report = "Reliable scorer from outside the paint."
        else:
            shoot_agg.agg_report = "Deadly shooter from all over the court."

        shoot_agg.grade(shoot_grade)
        self.aggs.append(shoot_agg)


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
