__author__ = 'Alex'

import Team
import RosterManager

class GameSim:

    def SimGame(self, home, away, db):
        home_starters = home.get_five(db)
        away_starters = away.get_five(db)

        self.PrintTeamStarters(home_starters , away_starters)

    def PrintTeamStarters(self, home_starters, away_starters):
        print("At Point Guard: " + home_starters[0].lnm + ", " +
              str(home_starters[0].agg["ovr"]) + " vs " +
                away_starters[0].lnm + ", "+ str(home_starters[0].agg["ovr"]))
        print("At Shooting Guard: " + home_starters[1].lnm + ", " +
              str(home_starters[1].agg["ovr"]) + " vs " +
                away_starters[1].lnm + ", "+ str(home_starters[1].agg["ovr"]))
        print("At Small Forward: " + home_starters[2].lnm + ", " +
              str(home_starters[2].agg["ovr"]) + " vs " +
                away_starters[2].lnm + ", "+ str(home_starters[2].agg["ovr"]))
        print("At Power Forward: " + home_starters[3].lnm + ", " +
              str(home_starters[3].agg["ovr"]) + " vs " +
                away_starters[3].lnm + ", "+ str(home_starters[3].agg["ovr"]))
        print("At Center: " + home_starters[4].lnm + ", " +
              str(home_starters[4].agg["ovr"]) + " vs " +
                away_starters[4].lnm + ", "+ str(home_starters[4].agg["ovr"]))