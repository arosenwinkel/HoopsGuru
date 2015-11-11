# GameState

import RosterManager
import os.path


class State:  # what is instantiated when the user opens the game
    def __init__(self):
        self.db_loaded = False  # nothing loaded yet, don't start the game
        self.db_name = "No DB Loaded"

    def print_roster(self):
        self.db.cursor.execute("SELECT * FROM Players")
        fun = ["rng", "lay", "ofw", "tou", "hnd", "box", "scn", "dfw", "pas", "off"]
        ath = ["qui", "vrt", "str", "spd", "fit", "coo"]
        iq = ["dec", "rct", "obl", "ant", "vis", "crt", "foc"]
        for i in range(1, 11):
            this_p = self.db.read_player(i)
            print("Player {}: {} {}, template: {}, {} height, {} wingspan, {} weight".format(
                this_p.id, this_p.fnm, this_p.lnm, this_p.tmp, this_p.hgt, this_p.wng, this_p.wgt
            ))
            for x in fun:
                print(x + "={},".format(this_p.fun[x]), end=" ")
            print()
            for x in ath:
                print(x + "={},".format(this_p.ath[x]), end=" ")
            print()
            for x in iq:
                print(x + "={},".format(this_p.iq[x]), end=" ")
            print()
            print()

    def new_game(self):  # create a new save
        while True:
            print("Please enter a name for your save.")
            response = input()

            dbname = response + ".univ"
            if not os.path.isfile(dbname):  # if the database does not already exist
                self.db = RosterManager.DB(dbname)  # make and init a new one
                print("Game saved as '{}'".format(dbname))  # confirmation
                self.db_name = dbname
                self.db_loaded = True
                break
            else:
                print("'{}' already exists.".format(dbname))  # error

    def load_game(self):  # load a game that already exists
        while True:
            print("Please enter the name of a saved game.")
            response = input()

            dbname = response + ".univ"
            if os.path.isfile(dbname):  # if the db exists
                self.db = RosterManager.DB(dbname)  # connect to it (not create it)
                print("'{}' loaded successfully.".format(dbname))
                self.db_name = dbname
                self.db_loaded = True
                break
            else:
                print("'{}' does not exist.".format(dbname))  # error

    def acquire_data(self):  # either create a new save or load one
        while True:
            if self.db_loaded:
                print("DB Loaded: {}".format(self.db_name))
            print("Please enter a command.")
            print("Available commands: (N)ew Game | (L)oad Game | (P)rint | (Q)uit")
            response = input()

            if response in "Nn":  # dispatcher
                self.new_game()

                print("Automatically creating players:")
                for i in range(10):
                    self.db.create_player()

            elif response in "Ll":
                self.load_game()

            elif response in "Pp":
                if self.db_loaded:
                    self.print_roster()
                else:
                    print("No DB loaded. Please load a database before printing.")

            elif response in "Qq":
                break

        if self.db_loaded:  # game ended, close the db
            self.db.close()

