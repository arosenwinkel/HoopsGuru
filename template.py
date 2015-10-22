# template.py
import random


def weighted_choice(choices):  # takes in a dictionary as an argument
    total = sum(w for c, w in choices.items())
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices.items():
        if upto + w > r:
            return c
        upto += w


class Template:
    def __init__(self, name, data_list):
        self.template_name = name
        self.fun = {}  # dict for fundamental skills
        self.ath = {}  # dict for athletic attributes
        self.iq = {}  # dict for bbiq attributes
        self.men = {}  # dict for mental attributes

        i = 0
        self.base_height = data_list[i]
        i += 1
        self.base_ws_factor = data_list[i]
        i += 1
        self.base_weight_factor = data_list[i]
        i += 1

        # fundamental skills
        self.fun["rng"] = data_list[i]  # shooting range
        i += 1
        self.fun["lay"] = data_list[i]  # layup
        i += 1
        self.fun["ofw"] = data_list[i]  # offensive footwork
        i += 1
        self.fun["tou"] = data_list[i]  # touch
        i += 1
        self.fun["hnd"] = data_list[i]  # handling
        i += 1
        self.fun["box"] = data_list[i]  # boxout
        i += 1
        self.fun["scn"] = data_list[i]  # set screen
        i += 1
        self.fun["dfw"] = data_list[i]  # defensive footwork
        i += 1
        self.fun["pas"] = data_list[i]  # passing
        i += 1
        self.fun["off"] = data_list[i]  # off-hand
        i += 1

        # athleticism
        self.ath["qui"] = data_list[i]  # quickness
        i += 1
        self.fun["vrt"] = data_list[i]  # vertical leap
        i += 1
        self.fun["str"] = data_list[i]  # strength
        i += 1
        self.fun["spd"] = data_list[i]  # speed
        i += 1
        self.fun["fit"] = data_list[i]  # fitness
        i += 1
        self.fun["coo"] = data_list[i]  # coordination
        i += 1

        # basketball iq
        self.iq["dec"] = data_list[i]  # decisions
        i += 1
        self.iq["rct"] = data_list[i]  # reaction time
        i += 1
        self.iq["obl"] = data_list[i]  # off-ball movement
        i += 1
        self.iq["ant"] = data_list[i]  # anticipation
        i += 1
        self.iq["vis"] = data_list[i]  # vision
        i += 1
        self.iq["crt"] = data_list[i]  # creativity
        i += 1
        self.iq["foc"] = data_list[i]  # focus
        i += 1

age_dist_ages = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
age_dist_wgts = [10, 14, 26, 35, 48, 40, 36, 43, 31, 34, 32, 18, 18, 15, 12, 17, 4, 4, 6, 3, 2, 1]
age_dist_dict = dict(zip(age_dist_ages, age_dist_wgts))

# Define template constants and then stick them all in a dictionary for access by other .py files
template_list = []
athletic_b = Template("athletic_b",[  # Dwight Howard, DeAndre Jordan,
    83.688, 1.051, 3.069,
    10, 10, 40, 40, 10, 40, 40, 25, 10, 10,
    75, 75, 90, 75, 75, 60,
    30, 30, 20, 30, 20, 20, 30])
template_list.append(athletic_b)

athletic_f = Template("athletic_f",[  # Kenneth Faried, Blake Griffin, Tristan Thompson, Montrezl Harrell
    80.667, 1.0597, 2.934,
    20, 20, 40, 40, 20, 40, 40, 30, 20, 20,
    80, 80, 80, 80, 80, 65,
    30, 30, 20, 30, 20, 20, 30])
template_list.append(athletic_f)

athletic_w = Template("athletic_w",[  # Stanley Johnson, Justise Winslow, Andre Wiggins, Kelly Oubre
    78.667, 1.0557, 2.627,
    30, 30, 30, 30, 30, 30, 20, 20, 30, 30,
    85, 90, 70, 85, 85, 70,
    30, 30, 30, 30, 20, 30, 30])
template_list.append(athletic_w)

athletic_g = Template( "athletic_g",[  # D'Angelo Russell, Westbrook, John Wall, Derrick Rose, Zach Lavine
    76.167, 1.0598, 2.563,
    35, 40, 20, 30, 40, 20, 20, 30, 40, 30,
    85, 90, 50, 90, 85, 80,
    30, 30, 30, 30, 30, 30, 30])
template_list.append(athletic_g)

scoring_g = Template( "scoring_g",[  # Steph Curry, Russell Westbrook, Damian Lillard, Dwyane Wade, Kyrie Irving
    75.2083, 1.03919, 2.5068,
    90, 90, 50, 90, 90, 30, 20, 30, 90, 90,
    80, 80, 30, 80, 85, 80,
    90, 50, 90, 50, 90, 90, 50])
template_list.append(scoring_g)

scoring_w = Template( "scoring_w",[  # MJ, Kobe, Klay Thompson, J.R. Smith, Nick Young, Demar Derozan
    78.625, 1.0462, 2.7114,
    90, 90, 50, 90, 90, 40, 30, 30, 80, 90,
    80, 80, 40, 80, 80, 70,
    90, 50, 90, 50, 80, 80, 50])
template_list.append(scoring_w)

scoring_f = Template( "scoring_f",[  # Melo, KD, Kevin Love, Anthony Bennett, Rudy Gay, Paul Pierce
    80.2917, 1.0650, 2.8924,
    90, 80, 70, 90, 70, 70, 70, 30, 60, 90,
    70, 70, 70, 70, 70, 70,
    90, 50, 90, 50, 70, 70, 50])
template_list.append(scoring_f)

scoring_b = Template( "scoring_b",[  # KG, Anthony Davis, LaMarcus Aldridge, Dirk, Chris Bosh, Marc Gasol
    83.70833, 1.05390, 2.8579,
    70, 50, 90, 90, 50, 80, 90, 30, 50, 90,
    60, 70, 80, 70, 60, 60,
    90, 50, 90, 50, 70, 70, 50])
template_list.append(scoring_b)
