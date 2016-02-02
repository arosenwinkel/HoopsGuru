# template.py


class Template:
    def __init__(self, name, pos1, pos2, quality, data_list):
        self.template_name = name
        self.pos1 = pos1
        self.pos2 = pos2
        # quality: 50 = NBA average, 70 = All-Star, 80 = All-NBA, 95 = GOAT
        self.quality = quality

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
        self.ath["vrt"] = data_list[i]  # vertical leap
        i += 1
        self.ath["str"] = data_list[i]  # strength
        i += 1
        self.ath["spd"] = data_list[i]  # speed
        i += 1
        self.ath["fit"] = data_list[i]  # fitness
        i += 1
        self.ath["coo"] = data_list[i]  # coordination
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
temp1 = Template("temp1", "SF", "PF", 95, [  # LeBron James, athletic versatile forward
    80, 1.053, 3.125,
    60, 75, 70, 80, 60, 55, 50, 75, 85, 70,
    80, 90, 85, 90, 85, 85,
    80, 80, 65, 75, 90, 80, 80
])
template_list.append(temp1)

temp2 = Template("temp2", "SF", "PF", 95, [  # Kevin Durant, scoring forward
    82.25, 1.079, 2.918,
    80, 70, 65, 80, 70, 45, 40, 65, 70, 75,
    75, 75, 65, 80, 80, 75,
    75, 70, 75, 70, 75, 80, 70
])
template_list.append(temp2)

temp3 = Template("temp3", "PG", "SG", 85, [  # Russell Westbrook, athletic scoring guard
    75.5, 1.056, 2.543,
    75, 80, 45, 70, 75, 50, 30, 50, 70, 80,
    95, 85, 50, 95, 90, 70,
    50, 60, 60, 55, 50, 60, 60
])
template_list.append(temp3)

temp4 = Template("temp4", "PG", "SG", 95, [  # Steph Curry, GOAT shooter
    75.25, 1.003, 2.525,
    95, 75, 30, 75, 90, 30, 20, 55, 80, 85,
    85, 50, 20, 70, 75, 80,
    70, 65, 85, 70, 85, 85, 65
])
template_list.append(temp4)

temp5 = Template("temp5", "C", "PF", 80, [  # DeMarcus Cousins, post scorer
    82.75, 1.085, 3.529,
    50, 40, 80, 85, 30, 75, 80, 40, 50, 70,
    60, 50, 80, 50, 50, 60,
    40, 40, 30, 35, 40, 35, 35
])
template_list.append(temp5)

temp6 = Template("temp6", "C", "None", 80, [  # Marc Gasol, versatile center
    85, 1.056, 3.118,
    50, 35, 70, 80, 20, 55, 65, 70, 65, 70,
    35, 35, 90, 40, 40, 55,
    50, 75, 30, 80, 45, 30, 75
])
template_list.append(temp6)

temp7 = Template("temp7", "PF", "None", 80, [  # Blake Griffin, athletic scorer
    82, 1.015, 3.061,
    40, 50, 60, 65, 40, 50, 60, 40, 55, 60,
    60, 80, 80, 60, 60, 60,
    35, 40, 45, 40, 50, 35, 40
])
template_list.append(temp7)

temp8 = Template("temp8", "SG", "None", 85, [  # James Harden, scoring 2 guard
    77.25, 1.071, 2.874,
    80, 90, 50, 80, 85, 60, 35, 35, 60, 85,
    80, 65, 45, 80, 75, 90,
    60, 40, 75, 40, 75, 80, 35
])
template_list.append(temp8)

temp9 = Template("temp9", "SG", "SF", 95, [  # Michael Jordan, GOAT 2 guard
    78, 1.071, 2.769,
    70, 95, 70, 95, 80, 65, 40, 80, 60, 90,
    80, 95, 50, 80, 85, 90,
    75, 80, 65, 85, 75, 85, 90
])
template_list.append(temp9)

temp10 = Template("temp10", "C", "None", 85, [  # Dwight Howard, athletic rim protector
    82.25, 1.076, 2.918,
    25, 35, 50, 35, 20, 85, 75, 80, 30, 40,
    75, 80, 90, 70, 65, 50,
    35, 75, 20, 80, 30, 20, 80
])
template_list.append(temp10)

temp11 = Template("temp11", "PF", "None", 70, [  # Serge Ibaka, athletic rim protector, shoots 3's
    82, 1.073, 2.878,
    60, 30, 50, 35, 30, 80, 65, 80, 35, 40,
    70, 70, 80, 60, 60, 55,
    35, 75, 40, 75, 35, 25, 75
])
template_list.append(temp11)

temp12 = Template("temp12", "PG", "None", 90, [  # Chris Paul, undersized distributor, great defender
    73, 1.045, 2.438,
    70, 80, 30, 85, 95, 65, 30, 85, 95, 85,
    85, 45, 35, 80, 85, 90,
    90, 90, 75, 85, 95, 90, 90
])
template_list.append(temp12)

temp13 = Template("temp13", "PF", "C", 80, [  # LaMarcus Aldridge, versatile offensive big
    83.25, 1.066, 2.811,
    50, 40, 80, 85, 45, 85, 70, 70, 50, 65,
    60, 50, 80, 65, 55, 70,
    60, 65, 45, 70, 50, 30, 55
])
template_list.append(temp13)

temp14 = Template("temp14", "PF", "None", 50, [  # Brandon MF Bass, Average PF
    79.25, 1.091, 3.104,
    35, 30, 45, 55, 25, 75, 50, 25, 40, 45,
    50, 60, 70, 50, 65, 70,
    40, 60, 20, 50, 20, 15, 45
])
template_list.append(temp14)

temp15 = Template("temp15", "SF", "SG", 50, [  # Wesley Johnson, Average Wing
    79.25, 1.066, 2.5994,
    70, 40, 30, 45, 40, 30, 20, 35, 25, 30,
    75, 80, 60, 80, 75, 70,
    40, 35, 50, 30, 20, 25, 40
])
template_list.append(temp15)

temp16 = Template("temp16", "PG", "SG", 50, [  # Jimmer Fredette, Really good in college
    74.5, 1.027, 2.631,
    90, 50, 25, 45, 65, 30, 15, 30, 60, 50,
    50, 30, 25, 70, 70, 75,
    45, 40, 70, 35, 60, 55, 40
])
template_list.append(temp16)

temp17 = Template("temp17", "PG", "None", 55, [  # Isaiah Thomas, Very undersized PG, 6MOY candidate
    70.25, 1.050, 2.633,
    65, 50, 15, 65, 70, 30, 20, 50, 50, 65,
    85, 50, 15, 85, 80, 80,
    45, 40, 50, 45, 30, 60, 35
])
template_list.append(temp17)

temp18 = Template("temp18", "SF", "None", 50, [  # Luol Deng, Versatile SF
    80, 1.056, 2.75,
    50, 45, 40, 45, 50, 55, 30, 60, 40, 40,
    70, 65, 40, 70, 90, 65,
    45, 60, 55, 60, 40, 35, 65
])
template_list.append(temp18)

temp19 = Template("temp19", "SG", "SF", 75, [  # Jimmy Butler, All-Star Wing, good defense
    79.75, 0.9969, 2.786,
    70, 70, 55, 60, 50, 40, 40, 80, 45, 50,
    70, 65, 75, 70, 90, 75,
    60, 80, 50, 75, 45, 40, 85
])
template_list.append(temp19)

temp20 = Template("temp20", "SG", "SF", 70, [  # Klay Thompson, All-Star Wing, great shooting
    79.25, 1.022, 2.594,
    90, 40, 45, 50, 40, 45, 35, 75, 40, 35,
    65, 60, 65, 60, 75, 70,
    60, 80, 80, 75, 40, 35, 80 
])
template_list.append(temp20)

temp21 = Template("temp21", "SG", "SF", 80, [  # Kawhi Leonard, GOAT wing defender
    79, 1.101, 2.878,
    80, 55, 50, 65, 50, 50, 45, 90, 45, 50,
    75, 80, 75, 75, 85, 85,
    65, 95, 65, 90, 40, 35, 90
])
template_list.append(temp21)
