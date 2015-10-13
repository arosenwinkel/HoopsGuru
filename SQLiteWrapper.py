# SQLiteWrapper

import sqlite3

class DB: # generic DB connection
	def __init__(self, db_name): # create a new DB
		self.db_object = sqlite3.connect(db_name)
		self.cursor = self.db_object.cursor()
		self.name = db_name
	
	def close(self):
		self.db_object.close()
		
	def initRoster(self):
		# create table for players
		# ID is the unique identifier for each player
		# every player to ever exist in a game has a unique id (they are not reassigned after retirement)
		self.cursor.execute('''
						CREATE TABLE players
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