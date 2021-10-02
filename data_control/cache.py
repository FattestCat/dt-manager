from collections.abc import Callable
import data_control.team_struct as ts
from copy import deepcopy

class Cache:
    _instance = None
    data: list[ts.Team] = [ ]

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def cache(self, teams: list[ts.Team]) -> None:
        self.data = deepcopy(teams)
