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
        print("Template: {}".format(self.this_player.tmp))
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
        size_grade += gfr( height, 57, 77, 50)
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
        if ws < 74:
            size_agg.add_skill("Poor length for his position.")
        elif ws < 78:
            size_agg.add_skill("Average length for his position.")
        elif ws < 81:
            size_agg.add_skill("Good length for his position.")
        elif ws < 84:
            size_agg.add_skill("Exceptional wingspan at {}".format(repr_length(ws)))
        else:
            size_agg.add_skill("Freakish wingspan at {}".format(repr_length(ws)))

        if size_grade < 20:
            size_agg.agg_report = "Size really hurts him at this level."
        elif size_grade < 40:
            size_agg.agg_report = "Below average size."
        elif size_grade < 60:
            size_agg.agg_report = "Average size."
        elif size_grade < 80:
            size_agg.agg_report = "Good size."
        else:
            size_agg.agg_report = "Elite size for his position."

        size_agg.grade(size_grade)
        self.aggs.append(size_agg)

        ''' ATHLETICISM AGGREGATE '''
        ath_agg = Aggregate("Athleticism")
        ath_grade = 0

        quickness = self.this_player.ath["qui"]
        ath_grade += gfr( quickness, 50, 85, 20 )
        if quickness < 50:
            ath_agg.add_skill("No explosiveness to speak of.")
        elif quickness < 75:
            ath_agg.add_skill("Not exceptionally explosive.")
        elif quickness < 85:
            ath_agg.add_skill("Good explosiveness.")
        else:
            ath_agg.add_skill("Incredibly explosive.")

        vertical = self.this_player.ath["vrt"]
        ath_grade += gfr( vertical, 30, 85, 20 )
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
        ath_grade += gfr( speed, 50, 85, 20 )
        if speed < 50:
            ath_agg.add_skill("Too slow on the open floor.")
        elif speed < 75:
            ath_agg.add_skill("Average speed on the open floor.")
        elif speed < 85:
            ath_agg.add_skill("Good speed on the open floor.")
        else:
            ath_agg.add_skill("Excellent speed on the open floor.")

        nat_fit = self.this_player.ath["fit"]
        ath_grade += gfr( nat_fit, 40, 80, 20 )
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

        shoot_grade += gfr( height, 67, 76, 10)
        if height < 73:
            shoot_agg.add_skill("Has difficulty getting his shot off against taller players.")
        elif height > 75:
            shoot_agg.add_skill("No trouble getting his shot off over defenders.")

        rng = self.this_player.fun["rng"]
        shoot_grade += gfr( rng, 1, 85, 30 )
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

        handling = self.this_player.fun["hnd"]
        shoot_grade += gfr( handling, 1, 85, 20 )
        if handling < 20:
            shoot_agg.add_skill("No scoring ability off the dribble.")
        elif handling < 40:
            shoot_agg.add_skill("Rarely able to hit jumpers off of the dribble.")
        elif handling < 60:
            shoot_agg.add_skill("Can sometimes make jumpers off of the dribble.")
        elif handling < 80:
            shoot_agg.add_skill("Comfortable hitting jumpers off of the dribble.")
        else:
            shoot_agg.add_skill("Deadly hitting jumpers off of the dribble.")

        off_ball = self.this_player.iq["obl"]
        shoot_grade += gfr( off_ball, 1, 85, 20 )
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
        shoot_grade += gfr( consistency, 1, 60, 20 )
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
            att_agg.add_skill("Height really limits his finishing.")
        elif height > 75:
            att_agg.add_skill("Height allows him to finish in the paint.")

        layup = self.this_player.fun["lay"]
        att_grade += gfr( layup, 1, 85, 10 )
        if layup < 30:
            att_agg.add_skill("Not skilled enough to finish difficult layups.")
        elif layup < 50:
            att_agg.add_skill("Has a hard time converting difficult layups.")
        elif layup < 80:
            att_agg.add_skill("Converts difficult layups around defenders.")
        else:
            att_agg.add_skill("Uses a variety of acrobatic layups to finish around defenders with ease.")

        off_ftw = self.this_player.fun["ofw"]
        att_grade += gfr( off_ftw, 1, 75, 5 )
        if off_ftw < 25:
            att_agg.add_skill("Poor footwork when finishing in the paint.")
        elif off_ftw > 50:
            att_agg.add_skill("Good footwork gives him more opportunities in the paint.")

        touch = self.this_player.fun["tou"]
        att_grade += gfr( touch, 1, 85, 15 )
        if touch < 30:
            att_agg.add_skill("No touch around the rim.")
        elif touch < 50:
            att_agg.add_skill("Shows little touch around the rim.")
        elif touch < 80:
            att_agg.add_skill("Soft shooting touch around the rim.")
        else:
            att_agg.add_skill("Terrific touch around the rim.")

        handling = self.this_player.fun["hnd"]
        att_grade += gfr( handling, 1, 85, 15 )
        if handling < 30:
            att_agg.add_skill("Lacks the ball-handling skills necessary to run the offense.")
        elif handling < 50:
            att_agg.add_skill("Ball handling could stand to improve.")
        elif handling < 80:
            att_agg.add_skill("Smooth handling the ball.")
        else:
            att_agg.add_skill("Easily loses his man with an array of ball-handling moves.")

        off_hand = self.this_player.fun["off"]
        att_grade += gfr( off_hand, 1, 85, 10 )
        if off_hand < 30:
            att_agg.add_skill("Avoids using his off-hand as much as possible.")
        elif off_hand < 50:
            att_agg.add_skill("Sometimes uncomfortable with using his off-hand.")
        elif off_hand < 80:
            att_agg.add_skill("Uses his off-hand well to keep the defense off-guard.")
        else:
            att_agg.add_skill("Finishes equally with both hands.")

        vertical = self.this_player.ath["vrt"]
        att_grade += gfr( vertical, 1, 85, 10 )
        if vertical < 30:
            att_agg.add_skill("Plays exclusively below the rim.")
        elif vertical < 50:
            att_agg.add_skill("Limited leaping ability can hinder his finishing.")
        elif vertical < 80:
            att_agg.add_skill("Able to play above the rim to aid his finishing.")
        else:
            att_agg.add_skill("Explosive leaping allows him to easily make plays above the rim.")

        quickness = self.this_player.ath["qui"]
        att_grade += gfr( quickness, 1, 85, 10 )
        if quickness < 30:
            att_agg.add_skill("Poor first step makes it hard to get separation from his man.")
        elif quickness < 50:
            att_agg.add_skill("Below average first step.")
        elif quickness < 80:
            att_agg.add_skill("Above average first step helps him drive to the basket.")
        else:
            att_agg.add_skill("Lightning first step allows him to beat his man with ease.")

        strength = self.this_player.ath["str"]
        att_grade += gfr( strength, 1, 60, 10 )
        if strength < 20:
            att_agg.add_skill("Too weak to finish through contact.")
        elif strength < 40:
            att_agg.add_skill("Uses his strength to finish through smaller defenders.")
        else:
            att_agg.add_skill("Strong enough to finish through larger defenders.")

        aggressiveness = self.this_player.men["agg"]
        att_grade += gfr( aggressiveness, 1, 85, 5 )
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

        pmk_grade += gfr( height, 67, 78, 10)
        if height < 72:
            pmk_agg.add_skill("Too short to see over the defense.")
        elif height > 75:
            pmk_agg.add_skill("Height allows him to see over the defense.")

        passing = self.this_player.fun["pas"]
        pmk_grade += gfr( passing, 1, 85, 20 )
        if passing < 30:
            pmk_agg.add_skill("Passing ability really limits ability to run the offense.")
        elif passing < 50:
            pmk_agg.add_skill("Only an adequate passer, can struggle making the simple play.")
        elif passing < 80:
            pmk_agg.add_skill("No problem making difficult passes.")
        else:
            pmk_agg.add_skill("Uses impressive arsenal of passes to distribute the ball.")

        handling = self.this_player.fun["hnd"]
        pmk_grade += gfr( handling, 1, 85, 10 )
        if handling < 30:
            pmk_agg.add_skill("Limited ball-handler.")
        elif handling < 50:
            pmk_agg.add_skill("Average ball-handling ability.")
        elif handling < 80:
            pmk_agg.add_skill("Uses ball-handling ability to create open shots for himself and others.")
        else:
            pmk_agg.add_skill("Uses incredible ball-handling ability to break ankles with ease.")

        decisions = self.this_player.iq["dec"]
        pmk_grade += gfr( decisions, 1, 85, 20 )
        if decisions < 30:
            pmk_agg.add_skill("Poor decision-making leads to costly turnovers.")
        elif decisions < 50:
            pmk_agg.add_skill("Can sometimes be pressured into poor decisions.")
        elif decisions < 80:
            pmk_agg.add_skill("Makes good decisions with the ball.")
        else:
            pmk_agg.add_skill("Excellent decision-making: sees the game in slow motion.")

        vision = self.this_player.iq["vis"]
        pmk_grade += gfr( vision, 1, 85, 20 )
        if vision < 30:
            pmk_agg.add_skill("Prone to tunnel vision when he has the ball.")
        elif vision < 50:
            pmk_agg.add_skill("Can occasionally miss open teammates with the ball.")
        elif vision < 80:
            pmk_agg.add_skill("Rarely misses playmaking opportunities with the ball.")
        else:
            pmk_agg.add_skill("Able to effortlessly find open shooters: eyes on the back of his head.")

        creativity = self.this_player.iq["crt"]
        pmk_grade += gfr( creativity, 1, 85, 10 )
        if creativity < 30:
            pass
        elif creativity < 50:
            pmk_agg.add_skill("Can be predictable at times.")
        elif creativity < 80:
            pass
        else:
            pmk_agg.add_skill("Creativity allows him to easily make plays that keep the defense guessing.")

        ego = self.this_player.men["ego"]
        pmk_grade += gfr( ego, 10, 60, 10 )
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
        # Def footwork, quickness, vertical, strength, fitness, coordination, decisions, reactions, anticipation,
        # focus, motor, wingspan

        pmd_agg = Aggregate("Perimeter Defense")
        pmd_grade = 0

        wingspan = self.this_player.wng
        pmd_grade += gfr( wingspan, 70, 84, 15)
        if wingspan < 74:
            pmd_agg.add_skill("Length greatly limits ability as a perimeter defender.")
        elif wingspan < 81:
            pass
        elif wingspan < 84:
            pmd_agg.add_skill("Uses long arms to bother his matchup.")
        else:
            pmd_agg.add_skill("Uses his freakish wingspan to smother his matchup.")


        d_ftw = self.this_player.fun["dfw"]
        pmd_grade += gfr( d_ftw, 1, 85, 10 )
        if d_ftw < 30:
            pmd_agg.add_skill("Poor defensive fundamentals.")
        elif d_ftw < 50:
            pmd_agg.add_skill("Acceptable defensive fundamentals.")
        elif d_ftw < 80:
            pmd_agg.add_skill("Good defensive fundamentals.")
        else:
            pmd_agg.add_skill("Uses exceptional defensive footwork to stay in front of quicker opponents.")

        quickness = self.this_player.ath["qui"]
        pmd_grade += gfr( quickness, 1, 85, 15 )
        if quickness < 30:
            pmd_agg.add_skill("Frequently exposed by quick ball-handlers.")
        elif quickness < 50:
            pmd_agg.add_skill("Below average lateral quickness.")
        elif quickness < 80:
            pmd_agg.add_skill("Above average lateral quickness.")
        else:
            pmd_agg.add_skill("Terrific lateral quickness.")

        vertical = self.this_player.ath["vrt"]
        pmd_grade += gfr( vertical, 1, 85, 5 )
        if vertical < 30:
            pmd_agg.add_skill("Doesn't have the leaping ability to contest shots effectively.")
        elif vertical < 50:
            pmd_agg.add_skill("Able to challenge shots from smaller opponents.")
        elif vertical < 80:
            pmd_agg.add_skill("Leaping ability improves ability to challenge perimeter shots.")
        else:
            pmd_agg.add_skill("Explosive leaping ability makes him a terror against jump-shooters.")

        strength = self.this_player.ath["str"]
        pmd_grade += gfr( strength, 1, 50, 5 )
        if strength < 30:
            pmd_agg.add_skill("Lack of strength gives him a hard time fighting through screens.")
        elif strength > 49:
            pmd_agg.add_skill("Easily fights through screens to challenge shooters.")

        fitness = self.this_player.ath["fit"]
        pmd_grade += gfr( fitness, 1, 85, 5 )
        if fitness < 30:
            pmd_agg.add_skill("Poor conditioning makes defense really suffer at the end of games.")
        elif fitness < 70:
            pass
        else:
            pmd_agg.add_skill("Able to chase quick guards around screens all night long.")

        coordination = self.this_player.ath["coo"]
        pmd_grade += gfr( coordination, 1, 85, 5 )
        if coordination < 30:
            pmd_agg.add_skill("Lacks the body control necessary to contest shots without fouling.")
        elif coordination < 50:
            pmd_agg.add_skill("Can sometimes be pump-faked into a foul.")
        elif coordination < 80:
            pass
        else:
            pmd_agg.add_skill("Impeccable body control makes it easy to defend without fouling.")

        decisions = self.this_player.iq["dec"]
        pmd_grade += gfr( decisions, 1, 85, 5 )
        if decisions < 30:
            pmd_agg.add_skill("Gambles for steals, giving up big plays.")
        elif decisions < 50:
            pmd_agg.add_skill("Sometimes displays poor decision making.")
        elif decisions < 80:
            pmd_agg.add_skill("Displays good decision making on defense.")
        else:
            pmd_agg.add_skill("Always knows when to play it safe and when to go for big plays.")

        reactions = self.this_player.iq["rct"]
        pmd_grade += gfr( reactions, 1, 85, 15 )
        if reactions < 30:
            pmd_agg.add_skill("Usually the last player on the court to notice loose balls.")
        elif reactions < 50:
            pmd_agg.add_skill("Sometimes a step slow reacting to opponents.")
        elif reactions < 80:
            pmd_agg.add_skill("Reacts well to quick opponents.")
        else:
            pmd_agg.add_skill("Able to seamlessly mirror opponents movements on defense.")

        anticipation = self.this_player.iq["ant"]
        pmd_grade += gfr( anticipation, 1, 85, 15 )
        if anticipation < 30:
            pmd_agg.add_skill("Always in the wrong place on defense.")
        elif anticipation < 50:
            pmd_agg.add_skill("Sometimes fails to anticipate, leaving him out of position.")
        elif anticipation < 80:
            pmd_agg.add_skill("Anticipates steals well.")
        else:
            pmd_agg.add_skill("Always in the right place at the right time on defense.")

        focus = self.this_player.iq["foc"]
        pmd_grade += gfr( focus, 1, 85, 10 )
        if focus < 30:
            pmd_agg.add_skill("Constantly loses his man when defending off-ball.")
        elif focus < 50:
            pmd_agg.add_skill("Can get caught ball-watching sometimes.")
        elif focus < 80:
            pmd_agg.add_skill("Rarely loses his man when defending off-ball.")
        else:
            pmd_agg.add_skill("Always defensively locked in.")

        motor = self.this_player.men["mtr"]
        pmd_grade += gfr( motor, 1, 85, 5 )
        if motor < 30:
            pmd_agg.add_skill("Gives up too easily on the play.")
        elif motor < 70:
            pass
        else:
            pmd_agg.add_skill("Refuses to give up on the play.")

        if pmd_grade < 20:
            pmd_agg.agg_report = "Limited perimeter defense."
        elif pmd_grade < 40:
            pmd_agg.agg_report = "Below average perimeter defense."
        elif pmd_grade < 60:
            pmd_agg.agg_report = "Average perimeter defender."
        elif pmd_grade < 80:
            pmd_agg.agg_report = "Skilled perimeter defender."
        else:
            pmd_agg.agg_report = "Lockdown perimeter defender."

        pmd_agg.grade(pmd_grade)
        self.aggs.append(pmd_agg)

        ''' REBOUNDING AGGREGATE '''
        # wingspan, boxout, vertical, strength, reactions, anticipation, aggressiveness, motor

        reb_agg = Aggregate("Rebounding")
        reb_grade = 0

        wingspan = self.this_player.wng
        reb_grade += gfr( wingspan, 67, 84, 20)
        if wingspan < 78:
            reb_agg.add_skill("Lack of length greatly limits ability as a rebounder.")
        elif wingspan < 81:
            reb_agg.add_skill("Only average length for the position.")
        elif wingspan < 84:
            reb_agg.add_skill("Uses his long arms to pull down tough rebounds.")
        else:
            reb_agg.add_skill("Incredible wingspan makes him a natural rebounder.")

        boxout = self.this_player.fun["box"]
        reb_grade += gfr( boxout, 1, 50, 15 )
        if boxout < 20:
            reb_agg.add_skill("Constantly loses track of his man when boxing out.")
        elif boxout < 40:
            reb_agg.add_skill("Below average rebounding fundamentals.")
        elif boxout < 60:
            reb_agg.add_skill("Boxes out well to secure boards for his team.")
        else:
            reb_agg.add_skill("Always boxes his man out to ensure that his team gets the rebound.")

        vertical = self.this_player.ath["vrt"]
        reb_grade += gfr( vertical, 1, 85, 15 )
        if vertical < 30:
            reb_agg.add_skill("Poor leaper.")
        elif vertical < 50:
            reb_agg.add_skill("Below-average leaping ability.")
        elif vertical < 80:
            reb_agg.add_skill("Impressive vertical leaping ability.")
        else:
            reb_agg.add_skill("Incredibly explosive leaper.")

        strength = self.this_player.ath["str"]
        reb_grade += gfr( strength, 1, 50, 10 )
        if strength < 20:
            reb_agg.add_skill("Lack of strengths makes it easy to snatch rebounds out of his hands.")
        elif strength < 40:
            reb_agg.add_skill("Can sometimes be overpowered by bigger opponents.")
        elif strength < 60:
            reb_agg.add_skill("Good strength for his position")
        else:
            reb_agg.add_skill("Able to wrestle tough rebounds away from bigger defenders.")

        reactions = self.this_player.iq["rct"]
        reb_grade += gfr( reactions, 1, 80, 10 )
        if reactions < 30:
            reb_agg.add_skill("Has a hard time reacting to the ball once it hits the rim.")
        elif reactions < 50:
            reb_agg.add_skill("Not very quick to react to the ball once it hits the rim.")
        elif reactions < 80:
            reb_agg.add_skill("Makes adjustments once the ball hits the rim.")
        else:
            reb_agg.add_skill("Easily makes adjustments on the fly to grab difficult boards.")

        anticipation = self.this_player.iq["ant"]
        reb_grade += gfr( anticipation, 1, 80, 10 )
        if anticipation < 30:
            reb_agg.add_skill("Shows little to no anticipation for the ball.")
        elif anticipation < 50:
            reb_agg.add_skill("Has a hard time anticipating which trajectory the ball will take.")
        elif anticipation < 80:
            reb_agg.add_skill("Anticipates the trajectory of the ball.")
        else:
            reb_agg.add_skill("Knows exactly where to be to have the best chance of securing the rebound.")

        aggressiveness = self.this_player.men["agg"]
        reb_grade += gfr( aggressiveness, 1, 80, 10 )
        if aggressiveness < 30:
            reb_agg.add_skill("Avoids contact whenever possible when rebounding.")
        elif aggressiveness < 50:
            reb_agg.add_skill("Sometimes seems afraid to go for tough rebounds.")
        elif aggressiveness < 80:
            reb_agg.add_skill("No problem going for tough rebounds.")
        else:
            reb_agg.add_skill("Fearless in his pursuit of difficult rebounds.")

        motor = self.this_player.men["mtr"]
        reb_grade += gfr( motor, 1, 80, 10 )
        if motor < 30:
            reb_agg.add_skill("Gives up on rebounds that aren't near him.")
        elif motor < 50:
            pass
        elif motor < 80:
            reb_agg.add_skill("Hustles to grab far-away rebounds.")
        else:
            reb_agg.add_skill("Relentlessly pursues all possible.")

        if reb_grade < 20:
            reb_agg.agg_report = "Limited rebounder."
        elif reb_grade < 40:
            reb_agg.agg_report = "Below average rebounding ability."
        elif reb_grade < 60:
            reb_agg.agg_report = "Average rebounding ability."
        elif reb_grade < 80:
            reb_agg.agg_report = "Good rebounder."
        else:
            reb_agg.agg_report = "Excellent rebounder."

        reb_agg.grade(reb_grade)
        self.aggs.append(reb_agg)

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
