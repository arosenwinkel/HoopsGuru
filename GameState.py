# GameState

import RosterManager
import os
import os.path
import utilities
import Scouting


class State:  # what is instantiated when the user opens the game
    def __init__(self):
        self.db_loaded = False  # nothing loaded yet, don't start the game
        self.db_name = "No DB Loaded"
        self.db = "NULL"

    def print_roster(self):
        # create some lists for easy printout later....
        fun = ["rng", "lay", "ofw", "tou", "hnd", "box", "scn", "dfw", "pas", "off"]
        ath = ["qui", "vrt", "str", "spd", "fit", "coo"]
        iq = ["dec", "rct", "obl", "ant", "vis", "crt", "foc"]

        for i in range(1, 1000 + 1):
            this_p = self.db.read_player(i)  # read the player in
            print("Player {}: {} {}, template: {}, {}/{}, {} y.o. {} height, {} wingspan, {} lbs.".format(
                this_p.id, this_p.fnm, this_p.lnm, this_p.tmp, this_p.ps1, this_p.ps2, this_p.age,
                utilities.height_to_feet(this_p.hgt), utilities.height_to_feet(this_p.wng), this_p.wgt
            ))
            for x in fun:  # print out all attributes in the fundamental category
                print(x + "={},".format(this_p.fun[x]), end=" ")
            print()
            for x in ath:
                print(x + "={},".format(this_p.ath[x]), end=" ")
            print()
            for x in iq:
                print(x + "={},".format(this_p.iq[x]), end=" ")
            print()
            print()

    def scout(self):
        for i in range(1, 1000+1):
            this_p = self.db.read_player(i)
            s = Scouting.scout_pro_primary(this_p)
            s.scout()
            s.print()

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
            # print out the names of the saved games in this directory
            files_list = [f for f in os.listdir(".") if f[-5:] == ".univ"]  # files_list = list of save names
            if len(files_list):  # if there are saved games
                print("Saved games in this directory: {}".format(len(files_list)))
                for f in files_list:
                    print(f)
            else:
                print("No saves in this directory. Would you like to create one?")
                answer = input()
                if answer in "yY":
                    self.new_game()
                    break

            print("Please enter the name of a saved game.")
            dbname = input()

            if dbname[-5:] != ".univ":
                dbname += ".univ"
            if os.path.isfile(dbname):  # if the db exists
                self.db = RosterManager.DB(dbname)  # connect to it (not create it)
                print("'{}' loaded successfully.".format(dbname))
                self.db_name = dbname
                self.db_loaded = True
                break
            else:
                print("'{}' does not exist. Would you like to create a new save?".format(dbname))  # error
                answer = input()
                if answer in "Yy":
                    self.new_game()
                    break
                else:
                    break

    def delete_game(self):
        while True:
            files_list = [f for f in os.listdir(".") if f[-5:] == ".univ"]  # files_list = list of save names
            if len(files_list):  # if there are saved games
                print("Saved games in this directory: {}".format(len(files_list)))
                for f in files_list:
                    print(f)
            else:
                print("No saves in this directory.")
                break

            print("Please enter the name of the game you would like to delete.")
            print("Press ENTER without typing anything to go back.")
            response = input()

            if response[-5:] == ".univ":
                pass
            else:
                response += ".univ"

            if response in files_list:
                print("Are you sure you want to delete {}? (y/N)".format(response))
                yesno = input()
                if yesno in "yY":
                    if self.db_name == response:
                        self.db_loaded = False  # nothing loaded yet, don't start the game
                        self.db_name = "No DB Loaded"
                        self.db = "NULL"
                    os.remove(response)
                    break
                else:
                    print("{} is not present in the directory.".format(response))

    def acquire_data(self):  # either create a new save or load one
        while True:
            if self.db_loaded:
                print("DB Loaded: {}".format(self.db_name))
            print("Please enter a command.")
            print("Available commands: (N)ew Game | (L)oad Game | (D)elete Game | (P)rint | (Q)uit")
            response = input()

            if response in "Nn":  # dispatcher
                self.new_game()

                print("Automatically creating players...", end="")
                amount = 1000
                for i in range(amount):
                    self.db.create_player()  # create, add to write queue
                print("done.")

                print("Writing players to the database...", end="")
                self.db.write_all()  # using this function to write the entire queue at once is much faster
                print("done.")

            elif response in "Ll":
                self.load_game()

            elif response in "Pp":
                if self.db_loaded:
                    self.scout()
                else:
                    print("No DB loaded. Please load a database before printing.")

            elif response in "dD":
                self.delete_game()

            elif response in "Qq":
                break

        if self.db_loaded:  # game ended, close the db
            self.db.close()
