__author__ = 'Alex'

import RosterManager

class Team:
    def __init__(self, name):

        self.name = name
        self.roster = []
        self.needs = {"C":0,"PF":0,"PG":0,"SG":0,"SF":0}

    def print_roster(self, db):
        db.cursor.execute("SELECT fnm,lst,ps1,ovr FROM players WHERE tm='"+ self.name +"' ORDER BY ovr DESC;")
        result_set = db.cursor.fetchall()
        print(result_set)
        print(self.needs)

    def update_roster(self, id, db):
        player = db.read_player(id)
        self.roster.append(player)
        self.needs[player.ps1] += player.agg["ovr"]

    def draft_player(self, db):
        #return the id of the player to draft

        if(len(self.roster) < 2):
            #sign the highest overall player available
            db.cursor.execute("SELECT id FROM players WHERE tm='Unassigned' ORDER BY ovr DESC LIMIT 1;")
            result_set = db.cursor.fetchall()
            id = result_set[0][0]
            self.update_roster(id, db)
            return id
        else:
            #sign based on needs
            position = min(self.needs, key=self.needs.get)
            db.cursor.execute("SELECT id FROM players WHERE tm='Unassigned' AND ps1='" + str(position) + "' ORDER BY ovr DESC LIMIT 1;")
            result_set = db.cursor.fetchall()
            if(len(result_set) != 0):
                id = result_set[0][0]
                self.update_roster(id, db)
                return id
            else:
                return -1
