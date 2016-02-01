__author__ = 'Alex'

import Team
import RosterManager

class InitialDraft:
    def __init__(self):

        self.team_names = ["Detroit","Los Angeles","Chicago",
                      "Houston","Philadelphia","Phoenix",
                      "Dallas","Austin","San Francisco",
                      "Indianapolis","Charlotte","Seattle",
                      "Portland","Denver","Washington",
                      "Memphis","Brooklyn","Boston",
                      "Baltimore","Oklahoma City","Louisville",
                      "Milwaukee","Sacramento","Atlanta",
                      "Miami","Cleveland","Oakland",
                      "Orlando","New York","Salt Lake City"]

        self.teams = []


    def draft(self, db):
        for i in self.team_names:
            team = Team.Team(i)
            self.teams.append(team)

        #completely random team for a player, testing purposes
        counter = 1
        while counter < 500:
            for i in self.teams:
                player = db.read_player(counter)
                i.add_player(player)
                db.cursor.execute("UPDATE players SET tm='" + i.name + "' WHERE id="+ str(player.id) +";")
                counter = counter + 1


        db.db_object.commit()



