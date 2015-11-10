# GameState

import RosterManager
import os.path


class State:  # what is instantiated when the user opens the game
    def __init__(self):
        self.db_loaded = False  # nothing loaded yet, don't start the game
        self.db_name = "No DB Loaded"

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
            print("Available commands: (N)ew Game | (L)oad Game | (Q)uit")
            response = input()

            if response in "Nn":  # dispatcher
                self.new_game()

                print("Automatically creating players:")
                for i in range(10):
                    self.db.create_player()

            elif response in "Ll":
                self.load_game()

                print("Automatically creating players:")
                for i in range(10):
                    self.db.create_player()

            elif response in "Qq":
                break

        if self.db_loaded:  # game ended, close the db
            self.db.close()

