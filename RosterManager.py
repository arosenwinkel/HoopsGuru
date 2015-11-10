# RosterManager

import sqlite3
import template
import random
import Player

def norm_int( n, std ):
    return int(random.gauss(n, std))

def norm_flt( n, std ):
    return random.gauss(n, std)

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
                      (ID integer PRIMARY KEY NOT NULL, fnm text, lst text, tm text, tmp text, ps1 integer, ps2 integer,
                         age integer, hgt integer, wgt integer, wng integer, fat integer, mot integer,
                         eth integer, tal integer, int integer, rng integer, lay integer, ofw integer,
                         tou integer, hnd integer, box integer, scn integer, dfw integer, pas integer,
                         ohn integer, qui integer, vrt integer, str integer, spd integer, fit integer,
                         coo integer, dec integer, rct integer, obl integer, ant integer, vis integer,
                         crt integer, foc integer, agg integer, cmp integer, mtr integer, cns integer,
                         clu integer, drt integer, mat integer, cch integer, dtr integer, ego integer,
                         ldr integer
                         )
                ''')

        self.db_object.commit()

    def create_player(self):
        new_id = self.first_free  # get the first player ID that is free
        this_template = random.choice(template.template_list)  # pick a template
        this_age = template.weighted_choice(template.age_dist_dict)  # pick an age

        p = Player.Player() # create player object to hold all the stats

        p.age = this_age
        p.height = norm_int(this_template.base_height, 1)  # get height
        p.wng = int(norm_flt(this_template.base_ws_factor, .01) * p.height)  # get wingspan
        p.wgt = int(norm_flt(this_template.base_weight_factor, .1) * p.height)  # get weight

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

        # print data
        print(new_id)
        print(this_template.template_name)
        print(this_age)
        print(p.height)
        print(p.wng)
        print(p.wgt)
        print(p.fun)
        print(p.ath)
        print(p.iq)
