# RosterManager

import sqlite3
import template
import random
import Player
import utilities


def norm_int(n, std):
    return int(random.gauss(n, std))


def norm_flt(n, std):
    return random.gauss(n, std)


class DB:  # generic DB connection
    def __init__(self, db_name):  # create a new DB OR connect to an existing one
        self.db_object = sqlite3.connect(db_name)
        self.cursor = self.db_object.cursor()
        self.name = db_name

        self.write_queue = []  # players to write into the DB

        self.init_roster()

        self.cursor.execute("SELECT MAX(ID) FROM players;")  # grab the max ID, set count to that
        self.count = self.cursor.fetchone()

        if self.count[0] is None:  # No players in the database yet
            self.count = 0
        else:
            self.count = int(self.count[0])

    @property
    def first_free(self):
        # returns the highest available player ID
        self.count += 1
        return self.count

    def close(self):
        self.db_object.close()

    def init_roster(self):
        # create table for players
        # ID is the unique identifier for each player
        # every player to ever exist in a game has a unique id (they are not reassigned after retirement)
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS players
                      (ID integer PRIMARY KEY NOT NULL, fnm text, lst text, tm text, tmp text, ps1 text, ps2 text,
                         age integer, hgt integer, wgt integer, wng integer, fat integer, mot integer,
                         eth integer, tal integer, inl integer, rng integer, lay integer, ofw integer,
                         tou integer, hnd integer, box integer, scn integer, dfw integer, pas integer,
                         off integer, qui integer, vrt integer, str integer, spd integer, fit integer,
                         coo integer, dec integer, rct integer, obl integer, ant integer, vis integer,
                         crt integer, foc integer, agg integer, cmp integer, mtr integer, cns integer,
                         clu integer, drt integer, mat integer, cch integer, dtr integer, ego integer,
                         ldr integer, sze integer, ath integer, sht integer, att integer, pmk integer,
                         per integer, reb integer, hlp integer, ins integer, pot integer, men integer,
                         dur integer, ovr integer
                         )
                ''')

        self.db_object.commit()
        
    def read_player(self, pid):  # read DB and return player at pid as a Player object
        # pid must be turned into a one-element tuple.... for some reason
        self.cursor.execute('SELECT * FROM players WHERE ID=?', (pid,))  # get the player with the correct ID
        data_list = self.cursor.fetchone()  # retrieve list of the player's attributes

        i = 0  # keep track of position (so this process is more updateable)
        
        p = Player.Player()

        [
            p.id, p.fnm, p.lnm, p.tm, p.tmp, p.ps1, p.ps2, p.age, p.hgt, p.wgt, p.wng,
            p.fat, p.mot, p.eth, p.tal, p.inl,
            p.fun["rng"], p.fun["lay"], p.fun["ofw"], p.fun["tou"], p.fun["hnd"], p.fun["box"],
            p.fun["scn"], p.fun["dfw"], p.fun["pas"], p.fun["off"],
            p.ath["qui"], p.ath["vrt"], p.ath["str"], p.ath["spd"], p.ath["fit"], p.ath["coo"],
            p.iq["dec"], p.iq["rct"], p.iq["obl"], p.iq["ant"], p.iq["vis"], p.iq["crt"], p.iq["foc"],
            p.men["agg"], p.men["cmp"], p.men["mtr"], p.men["cns"], p.men["clu"], p.men["drt"],
            p.men["mat"], p.men["cch"], p.men["dtr"], p.men["ego"], p.men["ldr"],
            p.agg["sze"], p.agg["ath"], p.agg["sht"], p.agg["att"], p.agg["pmk"], p.agg["per"],
            p.agg["reb"], p.agg["hlp"], p.agg["ins"], p.agg["pot"], p.agg["men"], p.agg["dur"], p.agg["ovr"]
        ] = data_list

        # tendencies to be added later....
        '''

        # shooting hotspots
        p.sht["rcr"] = data_list[i]  # right corner
        i += 1
        p.sht["lcr"] = data_list[i]
        i += 1
        p.sht["rwg"] = data_list[i]  # right wing
        i += 1
        p.sht["lwg"] = data_list[i]
        i += 1
        p.sht["tok"] = data_list[i]  # top of key (3PT)
        i += 1
        p.sht["ftl"] = data_list[i]  # free throw line (2PT)
        i += 1
        p.sht["rel"] = data_list[i]  # right elbow
        i += 1
        p.sht["lel"] = data_list[i]
        i += 1
        p.sht["rbl"] = data_list[i]  # right baseline
        i += 1
        p.sht["lbl"] = data_list[i]
        i += 1

        # tendencies....

        '''

        return p

    def create_player(self):
        new_id = self.first_free  # get the first player ID that is free
        this_template = random.choice(template.template_list)  # pick a template
        this_age = utilities.weighted_choice(template.age_dist_dict)  # pick an age

        p = Player.Player()

        name_generator = utilities.NameGenerator()
        choice = random.randint(0,1)
        p.fnm = name_generator.generate_first_name(choice)
        p.lnm = name_generator.generate_last_name(choice)

        p.id = new_id
        p.tmp = this_template.template_name

        # these stats are just temporary, for testing purposes

        p.age = this_age
        p.hgt = norm_int(this_template.base_height, 1)  # get height
        p.wng = int(norm_flt(this_template.base_ws_factor, .01) * p.hgt)  # get wingspan
        p.wgt = int(norm_flt(this_template.base_weight_factor, .1) * p.hgt)  # get weight

        p.ps1 = this_template.pos1
        p.ps2 = this_template.pos2

        # get all attributes
        for i in this_template.fun.keys():
            x = this_template.fun[i]
            x = norm_int(x, 3)
            x *= -.0022526 * (this_age ** 2) + .145624 * this_age - 1.327448
            p.fun[i] = int(x)

        for i in this_template.ath.keys():
            x = this_template.ath[i]
            x = norm_int(x, 3)
            x *= -.0021103 * (this_age ** 2) + .0981017 * this_age - .1806373
            p.ath[i] = int(x)

        for i in this_template.iq.keys():
            x = this_template.iq[i]
            x = norm_int(x, 3)
            x *= -.00170189 * (this_age ** 2) + .1247555 * this_age - 1.273465
            x = int(x)
            p.iq[i] = int(x)

        # mental attributes
        p.men["agg"] = 50  # aggressiveness
        p.men["cmp"] = 50  # composure
        p.men["mtr"] = 50  # motor
        p.men["cns"] = 50  # consistency
        p.men["clu"] = 50  # clutch
        p.men["drt"] = 50  # dirtiness
        p.men["mat"] = 50  # maturity
        p.men["cch"] = 50  # coachability
        p.men["dtr"] = 50  # determination
        p.men["ego"] = 50  # ego....
        p.men["ldr"] = 50  # leadership

        # init aggs to zero until scouted
        p.agg["sze"] = 0
        p.agg["ath"] = 0
        p.agg["sht"] = 0
        p.agg["att"] = 0
        p.agg["pmk"] = 0
        p.agg["per"] = 0
        p.agg["reb"] = 0
        p.agg["hlp"] = 0
        p.agg["ins"] = 0
        p.agg["pot"] = 0
        p.agg["men"] = 0
        p.agg["dur"] = 0
        p.agg["ovr"] = 0

        # shooting hotspots LEAVE OUT FOR NOW
        # p.sht["rcr"] = "50"  # right corner
        # p.sht["lcr"] = "50"
        # p.sht["rwg"] = "50"  # right wing
        # p.sht["lwg"] = "50"
        # p.sht["tok"] = "50"  # top of key (3PT)
        # p.sht["ftl"] = "50"  # free throw line (2PT)
        # p.sht["rel"] = "50"  # right elbow
        # p.sht["lel"] = "50"
        # p.sht["rbl"] = "50"  # right baseline
        # p.sht["lbl"] = "50"

        player_list = (p.id, p.fnm, p.lnm, p.tm, p.tmp, p.ps1, p.ps2, p.age, p.hgt, p.wgt, p.wng, p.fat, p.mot,
                       p.eth, p.tal, p.inl, p.fun["rng"], p.fun["lay"], p.fun["ofw"], p.fun["tou"], p.fun["hnd"],
                       p.fun["box"], p.fun["scn"], p.fun["dfw"], p.fun["pas"], p.fun["off"],
                       p.ath["qui"], p.ath["vrt"], p.ath["str"], p.ath["spd"], p.ath["fit"], p.ath["coo"],
                       p.iq["dec"], p.iq["rct"], p.iq["obl"], p.iq["ant"], p.iq["vis"], p.iq["crt"], p.iq["foc"],
                       p.men["agg"], p.men["cmp"], p.men["mtr"], p.men["cns"], p.men["clu"], p.men["drt"], p.men["mat"],
                       p.men["cch"], p.men["dtr"], p.men["ego"], p.men["ldr"], p.agg["sze"], p.agg["ath"], p.agg["sht"],
                       p.agg["att"], p.agg["pmk"], p.agg["pmd"], p.agg["reb"], p.agg["hlp"], p.agg["ins"], p.agg["pot"], 
                       p.agg["men"], p.agg["dur"], p.agg["ovr"])

        self.write_queue.append(player_list)

    def update_ovr(self, player_list):
        for p in player_list:
            query = ("UPDATE Players SET sze={:.0f}, ath={:.0f}, sht={:.0f}, att={:.0f}, pmk={:.0f}, per={:.0f}," +
                    " reb={:.0f}, hlp={:.0f}, ins={:.0f}, pot={:.0f}, men={:.0f}, dur={:.0f}, ovr={:.0f} "+
                    "WHERE ID={};").format(p.agg["sze"], p.agg["ath"], p.agg["sht"], p.agg["att"],
                    p.agg["pmk"], p.agg["pmd"], p.agg["reb"], p.agg["hlp"], p.agg["ins"], p.agg["pot"], p.agg["men"], 
                    p.agg["dur"], p.agg["ovr"], p.id )

            self.cursor.execute(query)

        self.db_object.commit()

    def write_all(self):
        for p in self.write_queue:  # for each player in the write queue....
            self.cursor.execute("INSERT INTO Players(ID, fnm, lst, tm, tmp, ps1, ps2, " +
                                "age, hgt, wgt, wng, fat, mot , " +
                                "eth, tal, inl, rng, lay, ofw , " +
                                "tou, hnd, box, scn, dfw, pas , " +
                                "off, qui, vrt, str, spd, fit , " +
                                "coo, dec, rct, obl, ant, vis , " +
                                "crt, foc, agg, cmp, mtr, cns , " +
                                "clu, drt, mat, cch, dtr, ego , " +
                                "ldr, sze, ath, sht, att, pmk , " +
                                "pmd, reb, hlp, ins, pot, men, dur, ovr) " +
                                "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?," +
                                "?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", p)

        self.db_object.commit()

        self.write_queue = []
