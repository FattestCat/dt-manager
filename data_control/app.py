from sqlalchemy.orm import Session
from database.db_control import DBControl

import time
from pprint import pprint
# from time import sleep

from LPparser.LPparser import *
from LPparser.LPcontrol import get_parsed_data
import cache
from control import cache_data, check_diff_teams,\
                    check_diff_players, no_changes,\
                    get_new_players, get_new_teams, get_updated_players,\
                    get_fount_players_count, get_cached_data


def main():

    p_data = get_parsed_data()

    print('-' * 70)
    pprint(p_data)
    
    db_c = DBControl("teams.db")
    db_c.create_db()
    db_c.create_all()

    with Session(db_c.engine) as session:
        from_db = db_c.get_all(session)
        cache_data(from_db["teams"], from_db["players"]) # type: ignore

    print('-' * 60)
    pprint(cache.teams)
    print('-' * 60)
    pprint(cache.players)

    check_diff_players(cache.players, p_data["players"]) # type: ignore
    check_diff_teams(cache.teams, p_data["teams"]) # type: ignore

    np = get_new_players()
    up = get_updated_players()
    nt = get_new_teams()
    print("New players".center(60, '-'))
    pprint(np)
    print("New teams".center(60, '-'))
    pprint(nt)
    print("Updated players".center(60, '-'))
    pprint(up)
    print(f'Number of new teams: {len(nt)}')
    print(f'Number of new players: {len(np)}')
    print(f'Number of updated plyaers: {len(up)}')
    print(f'Found players count: {get_fount_players_count()}')
    print(f'Number of players in db: {len(get_cached_data()["players"])}')


    # with Session(db_c.engine) as session:



    # with Session(db_c.engine) as session:
        # db_c.add_teams(session, p_data["teams"]) # type: ignore
        # db_c.add_players(session, p_data["players"]) # type: ignore
        # session.commit()

    # print('-' * 70)
    # with Session(db_c.engine) as session:
        # data = db_c.get_all(session)
        # pprint(data)
    
    # with Session(db_c.engine) as session:
        # print('-' * 70)
        # players = db_c.get_players_of_one_team(session, "4 Zoomers")
        # pprint(players)
    



if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)

    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
    # TODO: REDO ALL THIS SHIT
