# Player.py


class Player:
    def __init__(self):  # init a player object

        self.fun = {}  # dict for fundamental skills
        self.ath = {}  # dict for athletic attributes
        self.iq = {}  # dict for bbiq attributes
        self.men = {}  # dict for mental attributes
        self.sht = {}  # dict for shooting attributes
        self.id = 0
        self.fnm = "Unnamed"
        self.lnm = "Player"
        self.tm = "Unassigned"  # team
        self.tmp = "Unassigned"  # template
        self.ps1 = 1
        self.ps2 = 2
        self.age = 1
        self.hgt = 1
        self.wgt = 1
        self.wng = 1
        self.fat = 50
        self.mot = 50
        self.eth = 50
        self.tal = 50
        self.int = 50

    def read(self, db, pid):  # given an id, look the player up in the DB
        c = db.cursor  # get cursor object from DB
        c.execute('SELECT * FROM players WHERE ID=?', pid)  # get the player with the correct ID
        data_list = c.fetchone()  # retrieve list of the player's attributes

        print(data_list)  # debug

        i = 0  # keep track of position (so this process is more updateable)

        self.id = data_list[i]  # unique player ID
        i += 1
        self.fnm = data_list[i]  # first name
        i += 1
        self.lnm = data_list[i]  # last name
        i += 1
        self.tmp = data_list[i]  # player template
        i += 1
        self.ps1 = data_list[i]  # primary position
        i += 1
        self.ps2 = data_list[i]  # secondary position
        i += 1
        self.age = data_list[i]  # age....
        i += 1
        self.hgt = data_list[i]  # height (inches)
        i += 1
        self.wgt = data_list[i]  # weight (lbs)
        i += 1
        self.wng = data_list[i]  # wingspan (inches)
        i += 1
        self.fat = data_list[i]  # fatigue
        i += 1
        self.mot = data_list[i]  # motivation
        i += 1
        self.eth = data_list[i]  # work ethic
        i += 1
        self.tal = data_list[i]  # natural talent
        i += 1
        self.int = data_list[i]  # intelligence
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

        # mental attributes
        self.men["agg"] = data_list[i]  # aggressiveness
        i += 1
        self.men["cmp"] = data_list[i]  # composure
        i += 1
        self.men["mtr"] = data_list[i]  # motor
        i += 1
        self.men["cns"] = data_list[i]  # consistency
        i += 1
        self.men["clu"] = data_list[i]  # clutch
        i += 1
        self.men["drt"] = data_list[i]  # dirtiness
        i += 1
        self.men["mat"] = data_list[i]  # maturity
        i += 1
        self.men["cch"] = data_list[i]  # coachability
        i += 1
        self.men["dtr"] = data_list[i]  # determination
        i += 1
        self.men["ego"] = data_list[i]  # ego....
        i += 1

        # shooting hotspots
        self.sht["rcr"] = data_list[i]  # right corner
        i += 1
        self.sht["lcr"] = data_list[i]
        i += 1
        self.sht["rwg"] = data_list[i]  # right wing
        i += 1
        self.sht["lwg"] = data_list[i]
        i += 1
        self.sht["tok"] = data_list[i]  # top of key (3PT)
        i += 1
        self.sht["ftl"] = data_list[i]  # free throw line (2PT)
        i += 1
        self.sht["rel"] = data_list[i]  # right elbow
        i += 1
        self.sht["lel"] = data_list[i]
        i += 1
        self.sht["rbl"] = data_list[i]  # right baseline
        i += 1
        self.sht["lbl"] = data_list[i]
        i += 1

        # tendencies....
