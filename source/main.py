# main

import GameState


def main():
    state = GameState.State()
    state.acquire_data()
    if state.db_loaded:
        print("Database loaded. Proceed with game.")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
