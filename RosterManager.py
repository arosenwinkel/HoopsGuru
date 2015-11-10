# RosterManager

import sqlite3
import template
import random
import Player
import numpy


class DB:  # generic DB connection
    def __init__(self, db_name):  # create a new DB OR connect to an existing one
        self.db_object = sqlite3.connect(db_name)
        self.cursor = self.db_object.cursor()
        self.name = db_name

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
                      (ID  PRIMARY KEY NOT NULL, fnm text, lst text, tm text, tmp text, ps1 , ps2 ,
                         age , hgt , wgt , wng , fat , mot ,
                         eth , tal , int , rng , lay , ofw ,
                         tou , hnd , box , scn , dfw , pas ,
                         ohn , qui , vrt , str , spd , fit ,
                         coo , dec , rct , obl , ant , vis ,
                         crt , foc , agg , cmp , mtr , cns ,
                         clu , drt , mat , cch , dtr , ego ,
                         ldr
                         )
                ''')

        self.db_object.commit()

    def create_player(self):
        new_id = self.first_free
        this_template = random.choice(template.template_list)
        this_age = template.weighted_choice(template.age_dist_dict)

        print("ID: " + str(new_id))
        print("template name: " + str(this_template.template_name))
        print("Age: " + str(this_age))

        p = Player.Player()
        p.id = new_id

        #these stats are just temporary, for testing purposes
        p.fun["rng"] = "50"  # shooting range
        p.fun["lay"] = "50"  # layup
        p.fun["ofw"] = "50"  # offensive footwork
        p.fun["tou"] = "50"  # touch
        p.fun["hnd"] = "50"  # handling
        p.fun["box"] = "50"  # boxout
        p.fun["scn"] = "50"  # set screen
        p.fun["dfw"] = "50"  # defensive footwork
        p.fun["pas"] = "50"  # passing
        p.fun["off"] = "50"  # off-hand

        # athleticism
        p.ath["qui"] = "50"  # quickness
        p.ath["vrt"] = "50"  # vertical leap
        p.ath["str"] = "50"  # strength
        p.ath["spd"] = "50"  # speed
        p.ath["fit"] = "50"  # fitness
        p.ath["coo"] = "50"  # coordination

        # basketball iq
        p.iq["dec"] = "50"  # decisions
        p.iq["rct"] = "50"  # reaction time
        p.iq["obl"] = "50"  # off-ball movement
        p.iq["ant"] = "50"  # anticipation
        p.iq["vis"] = "50"  # vision
        p.iq["crt"] = "50"  # creativity
        p.iq["foc"] = "50"  # focus

        # mental attributes
        p.men["agg"] = "50"  # aggressiveness
        p.men["cmp"] = "50"  # composure
        p.men["mtr"] = "50"  # motor
        p.men["cns"] = "50"  # consistency
        p.men["clu"] = "50"  # clutch
        p.men["drt"] = "50"  # dirtiness
        p.men["mat"] = "50"  # maturity
        p.men["cch"] = "50"  # coachability
        p.men["dtr"] = "50"  # determination
        p.men["ego"] = "50"  # ego....
        p.men["ldr"] = "50"  # leadership

        # # shooting hotspots LEAVE OUT FOR NOW
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

        self.cursor.execute("INSERT INTO Players(ID, fnm, lst, tm, tmp, ps1, ps2, "
                         "age, hgt, wgt, wng, fat, mot , "
                         "eth, tal, int, rng, lay, ofw , "
                         "tou, hnd, box, scn, dfw, pas , "
                         "ohn, qui, vrt, str, spd, fit , "
                         "coo, dec, rct, obl, ant, vis , "
                         "crt, foc, agg, cmp, mtr, cns , "
                         "clu, drt, mat, cch, dtr, ego , "
                         "ldr) "
                            "VALUES (" + "'" +
                            str(new_id) + "'," +
                            "'"+ p.fnm + "'," +
                            "'"+p.lnm + "'," +
                            "'"+p.tm + "'," +
                            "'"+p.tmp + "'," +
                            "'"+p.ps1 + "'," +
                            "'"+p.ps2 + "'," +
                            "'"+p.age + "'," +
                            "'"+p.hgt + "'," +
                            "'"+p.wgt + "'," +
                            "'"+p.wng + "'," +
                            "'"+p.fat + "'," +
                            "'"+p.mot + "'," +
                            "'"+p.eth + "'," +
                            "'"+p.tal + "'," +
                            "'"+p.int + "'," +
                            "'"+p.fun["rng"] + "'," +
                            "'"+p.fun["lay"] + "'," +
                            "'"+p.fun["ofw"] + "'," +
                            "'"+p.fun["tou"] + "'," +
                            "'"+p.fun["hnd"] + "'," +
                            "'"+p.fun["box"] + "'," +
                            "'"+p.fun["scn"] + "'," +
                            "'"+p.fun["dfw"] + "'," +
                            "'"+p.fun["pas"] + "'," +
                            "'"+p.fun["off"] + "'," +
                            "'"+p.ath["qui"] + "'," +
                            "'"+p.ath["vrt"] + "'," +
                            "'"+p.ath["str"] + "'," +
                            "'"+p.ath["spd"] + "'," +
                            "'"+p.ath["fit"] + "'," +
                            "'"+p.ath["coo"] + "'," +
                            "'"+p.iq["dec"] + "'," +
                            "'"+p.iq["rct"] + "'," +
                            "'"+p.iq["obl"] + "'," +
                            "'"+p.iq["ant"] + "'," +
                            "'"+p.iq["vis"] + "'," +
                            "'"+p.iq["crt"] + "'," +
                            "'"+p.iq["foc"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["agg"] + "'," +
                            "'"+p.men["ldr"] + "');")

        self.db_object.commit()



