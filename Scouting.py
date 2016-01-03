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
        # Height, range, layup, offensive footwork, touch, handling, passing, off-hand, quickness, vertical,
        # strength, aggressiveness

        att_agg = Aggregate("Attacking")
        att_grade = 0

        att_grade += gfr( height, 70, 78, 10)
        if height < 73:
            shoot_agg.add_skill("Height really limits his finishing.")
        elif height > 75:
            shoot_agg.add_skill("Height allows him to finish in the paint.")

        layup = self.this_player.fun["lay"]
        att_grade += gfr( layup, 20, 95, 10 )
        if layup < 30:
            att_agg.add_skill("Not skilled enough to finish difficult layups.")
        elif layup < 50:
            att_agg.add_skill("Has a hard time converting difficult layups.")
        elif layup < 80:
            att_agg.add_skill("Converts difficult layups around defenders.")
        else:
            att_agg.add_skill("Uses a variety of acrobatic layups to finish around defenders with ease.")

        off_ftw = self.this_player.fun["ofw"]
        att_grade += gfr( off_ftw, 20, 75, 5 )
        if off_ftw < 25:
            att_agg.add_skill("Poor footwork when finishing in the paint.")
        elif off_ftw > 50:
            att_agg.add_skill("Good footwork gives him more opportunities in the paint.")

        touch = self.this_player.fun["tou"]
        att_grade += gfr( touch, 20, 95, 15 )
        if touch < 30:
            att_agg.add_skill("No touch around the rim.")
        elif touch < 50:
            att_agg.add_skill("Shows little touch around the rim.")
        elif touch < 80:
            att_agg.add_skill("Soft shooting touch around the rim.")
        else:
            att_agg.add_skill("Terrific touch around the rim.")

        handling = self.this_player.fun["hnd"]
        att_grade += gfr( handling, 20, 95, 15 )
        if handling < 30:
            att_agg.add_skill("Lacks the ball-handling skills necessary to run the offense.")
        elif handling < 50:
            att_agg.add_skill("Ball handling could stand to improve.")
        elif handling < 80:
            att_agg.add_skill("Smooth handling the ball.")
        else:
            att_agg.add_skill("Easily loses his man with an array of ball-handling moves.")

        off_hand = self.this_player.fun["off"]
        att_grade += gfr( off_hand, 20, 95, 10 )
        if off_hand < 30:
            att_agg.add_skill("Avoids using his off-hand as much as possible.")
        elif off_hand < 50:
            att_agg.add_skill("Sometimes uncomfortable with using his off-hand.")
        elif off_hand < 80:
            att_agg.add_skill("Uses his off-hand well to keep the defense off-guard.")
        else:
            att_agg.add_skill("Finishes equally with both hands.")

        vertical = self.this_player.ath["vrt"]
        att_grade += gfr( vertical, 20, 95, 10 )
        if vertical < 30:
            att_agg.add_skill("Plays exclusively below the rim.")
        elif vertical < 50:
            att_agg.add_skill("Limited leaping ability can hinder his finishing.")
        elif vertical < 80:
            att_agg.add_skill("Able to play above the rim to aid his finishing.")
        else:
            att_agg.add_skill("Explosive leaping allows him to easily make plays above the rim.")

        quickness = self.this_player.ath["qui"]
        att_grade += gfr( quickness, 20, 95, 10 )
        if quickness < 30:
            att_agg.add_skill("Poor first step makes it hard to get separation from his man.")
        elif quickness < 50:
            att_agg.add_skill("Below average first step.")
        elif quickness < 80:
            att_agg.add_skill("Above average first step helps him drive to the basket.")
        else:
            att_agg.add_skill("Lightning first step allows him to beat his man with ease.")

        strength = self.this_player.ath["str"]
        att_grade += gfr( strength, 10, 60, 10 )
        if strength < 20:
            att_agg.add_skill("Too weak to finish through contact.")
        elif strength < 40:
            att_agg.add_skill("Uses his strength to finish through smaller defenders.")
        else:
            att_agg.add_skill("Strong enough to finish through larger defenders.")

        aggressiveness = self.this_player.men["agg"]
        att_grade += gfr( aggressiveness, 20, 95, 5 )
        if aggressiveness < 30:
            att_agg.add_skill("Contact-shy around the rim.")
        elif aggressiveness < 50:
            att_agg.add_skill("Able to absorb contact in order to finish.")
        elif aggressiveness < 80:
            att_agg.add_skill("Willing to absorb contact in order to finish.")
        else:
            att_agg.add_skill("Fearless at driving to the rim.")

        if att_grade < 20:
            att_agg.agg_report = "Very poor finisher."
        elif att_grade < 40:
            att_agg.agg_report = "Below average finisher."
        elif att_grade < 60:
            att_agg.agg_report = "Average finisher."
        elif att_grade < 80:
            att_agg.agg_report = "Skilled finisher."
        else:
            att_agg.agg_report = "Fantastic finisher around the rim."

        att_agg.grade(att_grade)
        self.aggs.append(att_agg)

        ''' PLAYMAKING AGGREGATE '''
        # passing, handling, decision making, anticipation, court vision, creativity, ego

        pmk_agg = Aggregate("Playmaking")
        pmk_grade = 0

        pmk_grade += gfr( height, 70, 78, 10)
        if height < 72:
            pmk_agg.add_skill("Too short to see over the defense.")
        elif height > 75:
            pmk_agg.add_skill("Height allows him to see over the defense.")

        passing = self.this_player.fun["pas"]
        pmk_grade += gfr( passing, 30, 95, 10 )
        if passing < 30:
            pmk_agg.add_skill("Passing ability really limits ability to run the offense.")
        elif passing < 50:
            pmk_agg.add_skill("Only an adequate passer, can struggle making the simple play.")
        elif passing < 80:
            pmk_agg.add_skill("No problem making difficult passes.")
        else:
            pmk_agg.add_skill("Uses impressive arsenal of passes to distribute the ball.")

        handling = self.this_player.fun["hnd"]
        pmk_grade += gfr( handling, 30, 95, 10 )
        if handling < 30:
            pmk_agg.add_skill("Limited ball-handler.")
        elif handling < 50:
            pmk_agg.add_skill("Average ball-handling ability.")
        elif handling < 80:
            pmk_agg.add_skill("Uses ball-handling ability to create open shots for himself and others.")
        else:
            pmk_agg.add_skill("Uses incredible ball-handling ability to break ankles with ease.")

        decisions = self.this_player.iq["dec"]
        pmk_grade += gfr( decisions, 20, 95, 15 )
        if decisions < 30:
            pmk_agg.add_skill("Poor decision-making leads to costly turnovers.")
        elif decisions < 50:
            pmk_agg.add_skill("Can sometimes be pressured into poor decisions.")
        elif decisions < 80:
            pmk_agg.add_skill("Makes good decisions with the ball.")
        else:
            pmk_agg.add_skill("Excellent decision-making: sees the game in slow motion.")

        vision = self.this_player.iq["vis"]
        pmk_grade += gfr( vision, 20, 95, 15 )
        if vision < 30:
            pmk_agg.add_skill("Prone to tunnel vision when he has the ball.")
        elif vision < 50:
            pmk_agg.add_skill("Can occasionally miss open teammates with the ball.")
        elif vision < 80:
            pmk_agg.add_skill("Rarely misses playmaking opportunities with the ball.")
        else:
            pmk_agg.add_skill("Able to effortlessly find open shooters: eyes on the back of his head.")

        creativity = self.this_player.iq["crt"]
        pmk_grade += gfr( creativity, 20, 95, 10 )
        if creativity < 30:
            pass
        elif creativity < 50:
            pmk_agg.add_skill("Can be predictable at times.")
        elif creativity < 80:
            pass
        else:
            pmk_agg.add_skill("Creativity allows him to easily make plays that keep the defense guessing.")

        ego = self.this_player.men["ego"]
        pmk_grade += gfr( ego, 20, 95, 10 )
        if ego < 30:
            pmk_agg.add_skill("Notorious black hole for the ball.")
        elif ego < 50:
            pmk_agg.add_skill("Tends to over-dribble.")
        elif ego < 80:
            pmk_agg.add_skill("Doesn't let desire to score come before the team.")
        else:
            pmk_agg.add_skill("Selfless passer, prefers setting teammates up with easy scores.")

        if pmk_grade < 20:
            pmk_agg.agg_report = "Limited playmaking ability."
        elif pmk_grade < 40:
            pmk_agg.agg_report = "Below average playmaking ability."
        elif pmk_grade < 60:
            pmk_agg.agg_report = "Average playmaker."
        elif pmk_grade < 80:
            pmk_agg.agg_report = "Skilled playmaker."
        else:
            pmk_agg.agg_report = "Maestro of the half-court offense."

        pmk_agg.grade(pmk_grade)
        self.aggs.append(pmk_agg)


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
