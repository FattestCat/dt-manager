from collections.abc import Callable
import data_control.team_struct as ts

class Cache:

    teams: list[ts.Team] = [ ]

    def cache(self, tms: list[ts.Team]) -> None:
        self.teams = tms[:]
