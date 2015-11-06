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
temp1 = Template("temp1", [  # LeBron James
    80, 1.053, 3.125,
    60, 75, 70, 80, 60, 55, 50, 75, 85, 70,
    80, 90, 85, 90, 85, 85,
    80, 80, 65, 75, 90, 80, 80
])
template_list.append(temp1)

temp2 = Template("temp2", [  # Kevin Durant
    82.25, 1.079, 2.918,
    80, 70, 65, 80, 70, 45, 40, 65, 70, 75,
    75, 75, 65, 80, 80, 75,
    75, 70, 75, 70, 75, 80, 70
])
template_list.append(temp2)

temp3 = Template("temp3", [  # Russell Westbrook
    75.5, 1.056, 2.543,
    75, 80, 45, 70, 75, 50, 30, 50, 70, 80,
    90, 85, 50, 95, 90, 70,
    50, 60, 60, 55, 50, 60, 60
])
template_list.append(temp3)

temp4 = Template("temp4", [  # Steph Curry
    75.25, 1.003, 2.525,
    95, 75, 30, 75, 90, 30, 20, 55, 80, 85,
    85, 50, 20, 70, 75, 80,
    70, 65, 85, 70, 85, 85, 65
])
template_list.append(temp4)

temp5 = Template("temp5", [  # DeMarcus Cousins
    82.75, 1.085, 3.529,
    50, 40, 80, 85, 30, 75, 80, 40, 50, 70,
    60, 50, 80, 50, 50, 60,
    40, 40, 30, 35, 40, 35, 35
])
template_list.append(temp5)
