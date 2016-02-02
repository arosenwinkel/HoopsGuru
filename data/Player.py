# Player.py


class Player:
    def __init__(self):  # init a player object

        self.fun = {}  # dict for fundamental skills
        self.ath = {}  # dict for athletic attributes
        self.iq = {}  # dict for bbiq attributes
        self.men = {}  # dict for mental attributes
        self.sht = {}  # dict for shooting attributes
        self.agg = {}
        self.overall_agg = None
        self.id = 0
        self.fnm = "First"
        self.lnm = "Last"
        self.tm = "Unassigned"
        self.tmp = "Unassigned"
        self.ps1 = "None"
        self.ps2 = "None"
        self.age = 1
        self.hgt = 1
        self.wgt = 1
        self.wng = 1
        self.fat = 50
        self.mot = 50
        self.eth = 50
        self.tal = 50
        self.inl = 50

