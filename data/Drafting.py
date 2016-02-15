__author__ = 'Alex'

import Team
import RosterManager

class InitialDraft:

    def draft(self, db, teams):

        #completely random team for a player, testing purposes
        counter = 1
        while counter < 400:
            for i in teams:
                id = i.draft_player(db)
                if(id != -1):
                    db.cursor.execute("UPDATE players SET tm='" + i.name + "' WHERE id="+ str(id) +";")
                counter = counter + 1

        db.db_object.commit()




