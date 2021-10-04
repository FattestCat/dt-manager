from sqlalchemy.orm import Session
from database.db_control import DBControl

from pprint import pprint
# from time import sleep

from LPparser.LPparser import *
from LPparser.LPcontrol import get_parsed_data


def main():
    p_data = get_parsed_data()
    print('-' * 70)
    pprint(p_data)
    db_c = DBControl("teams.db")
    db_c.create_db()
    db_c.create_all()
    with Session(db_c.engine) as session:
        db_c.add_teams(session, p_data["teams"]) # type: ignore
        db_c.add_players(session, p_data["players"]) # type: ignore
        session.commit()

    print('-' * 70)
    with Session(db_c.engine) as session:
        data = db_c.get_all(session)
        pprint(data)
    
    with Session(db_c.engine) as session:
        print('-' * 70)
        players = db_c.get_players_of_one_team(session, "4 Zoomers")
        pprint(players)
    



if __name__ == '__main__':
    main()

    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
