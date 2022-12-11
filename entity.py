from colour_printer import fg, bg, util

class Entity:
    '''A representation of an entity existing on a map.'''
    def __init__(self, symbol, colour, name, position, solid=True, description=''):
        self.symbol = symbol
        self.colour = colour # (R, G, B)
        self.name = name
        self.position = position
        self.solid = solid
        self.description = description
        
    def __str__(self):
        return (
            f"{fg.rgb(self.colour[0], self.colour[1], self.colour[2])}" + 
            f"{self.symbol}{util.RESET}"
        )

    def clone(self, position=(0,0)):
        '''Returns new instances of entity with same attributes.'''
        return Entity(
            self.symbol,
            self.colour,
            self.name,
            self.position,
            self.solid,
            self.description
        )
        
    def print_extended(self):
        print(  f"\t\t{self}\n" + 
                f"\t{self.name}\n" + 
                f"\tDescription:\n\t\t{self.description}\n")

class Container(Entity):
    '''A representation of a physical container in the game.'''
    def __init__(
        self,
        symbol,
        colour,
        name,
        position,
        description='',
        inventory=[],
        key=None
    ):
        super().__init__(symbol, colour, name, position, True, description)
        self.inventory = inventory
        self.locked = False
        if key:
            self.locked = True

class Mob(Entity):
    '''A representation of an NPC in the game.'''
    def __init__(
        self,
        symbol,
        colour,
        name,
        position,
        health, # (current_health, max_health)
        stamina, # Points available for movement or actions.
        base_damage,
        faction, # The group the NPC is friendly to by default.
        solid=True,
        description='',
        inventory=[],
    ):
        super().__init__(symbol, colour, name, position, solid, description)
        self.health = health
        self.stamina = stamina
        self.base_damage = base_damage
        self.faction = faction
        # self.hostile = True if faction hostile to player faction, else False
        self.inventory = inventory