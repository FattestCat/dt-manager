from dataclasses import dataclass, field
from random import randint

@dataclass(order=True)
class Player:
    """Class describing player."""
    name: str = field(compare=False)
    position: int
    price: int
    salary: int
    laning: int
    agression: int
    map_awareness: int
    reaction_time: int
    farm_speed: int
    hero_pool: int

    # def __init__(self, position, laning, agression, map_awa, react_time, farm_speed, h_pool):
        # self.position = position
        # self.stats = dict()
        # self.stats["laning"] = laning
        # self.stats["agression"] = agression
        # self.stats["map awareness"] = map_awa
        # self.stats["reaction time"] = react_time
        # self.stats["farm speed"] = farm_speed
        # self.stats["hero pool"] = h_pool

    # def __str__(self):
        # profile = f"Position: {self.position}\n"

        # for stat in self.stats:
            # profile += f"{stat}: {self.stats[stat]}\n"

        # return profile

    @staticmethod
    def generate_blank_player():
        return Player(name="blanc",
                position=randint(1,5),
                price=randint(1, 5),
                salary=randint(100, 1000), 
                laning=randint(1, 10),
                agression=randint(1, 10),
                map_awareness=randint(1, 10),
                reaction_time=randint(1, 10),
                farm_speed=randint(1, 10),
                hero_pool=randint(1, 10))

