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

    def pull_roster_to_mem(self, db):
        db.cursor.execute("SELECT id FROM players WHERE tm='"+ self.name +"' ORDER BY ovr DESC;")
        result_set = db.cursor.fetchall()
        for i in result_set:
            self.update_roster(i[0],db)

    def get_five(self,db):
        #get 5 returns a list of the starting 5 players
        # ordered by position
        if len(self.roster) == 0:
            self.pull_roster_to_mem(db)
        starting_five = []
        positions = ["PG","SG","SF","PF","C"]
        # PG = 1, SG = 2, SF = 3, PF = 4, C = 5

        best_for_position = self.roster[0] #Placeholder value

        for pos in range(len(positions)):
            overall = 0
            for i in range(len(self.roster)):
                if self.roster[i].ps1 == positions[pos]:
                    if self.roster[i].agg["ovr"] > overall:
                        best_for_position = self.roster[i]
                        overall = best_for_position.agg["ovr"]
            starting_five.append(best_for_position)
        return starting_five

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
