# GameState

import SQLiteWrapper
import os.path

class State:
	def __init__(self):
		self.db_loaded = False
		
	def newGame(self):
		while True:
			print("Please enter a name for your save.")
			response = input()
			
			dbname = response + ".univ"
			if not os.path.isfile(dbname):
				self.db = SQLiteWrapper.DB(dbname)
				self.db.initRoster()
				print("Game saved as '{}'".format(dbname))
				self.db_loaded = True
				break
			else:
				print("'{}' already exists.".format(dbname))
		
	def loadGame(self):
		while True:
			print("Please enter the name of a saved game.")
			response = input()
			
			dbname = response + ".univ"
			if os.path.isfile(dbname):
				self.db = SQLiteWrapper.DB(dbname)
				print("'{}' loaded successfully.".format(dbname))
				self.db_loaded = True
				break
			else:
				print("'{}' does not exist.".format(dbname))
		
	def acquireData(self):
		while True:
			print("Please enter a command.")
			print("Available commands: (N)ew Game | (L)oad Game | (Q)uit")
			response = input()
			
			if response in "Nn":
				self.newGame()
				
			elif response in "Ll":
				self.loadGame()
				
			elif response in "Qq":
				break
		
		if self.db_loaded:
			self.db.close()