# main

import GameState

def main():
	state = GameState.State()
	state.acquireData()
	if state.db_loaded:
		print("Database loaded. Proceed with game.")
	
	print("Thanks for playing!")
	
main()