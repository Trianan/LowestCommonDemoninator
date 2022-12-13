from colour_printer import fg, bg, util
from operator import attrgetter

class Entity:
    '''A representation of an entity existing on a map.'''
    def __init__(
        self,
        symbol,
        colour,
        name,
        position,
        description='',
        solid=True
    ):
        self.symbol = symbol
        self.colour = colour
        self.name = name
        self.position = position
        self.description = description
        self.solid = solid
        
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
            self.description,
            self.solid,
        )

    def print_extended(self):
        '''Intended for displaying entitysets and in-game descriptions of entities.'''
        print(
            f"\t\t{self}\n" + 
            f"\t{self.name}\n" +
            f"\tEntity type: {type(self)}\n" +
            f"\tDescription:\n\t\t{self.description}\n" +
            f"\tsolid: {self.solid}\n\n"
        )


class Container(Entity):
    '''A representation of a physical container in the game.'''
    def __init__(
        self,
        inventory, # List of Items
        key, # Either a string, or falsy value if unlocked.
        *base_args # Rest of arguments for base Entity superclass.
    ):
        super().__init__(*base_args)
        self.inventory = inventory
        self.key = key
        self.locked = True if key else False

    def print_extended(self):
        super().print_extended()
        print(
            f"\tInventory: {self.inventory}\n" +
            f"\tLocked: {self.locked}\tKey: {self.key}\n\n"
        )

class Mob(Entity):
    '''A representation of an NPC in the game.'''
    def __init__(
        self,
        health, # (current_health, max_health)
        stamina, # (current, max); Points available for movement or actions.
        base_damage,
        faction, # The group the NPC is friendly to by default.
        inventory,
        *base_args
    ):
        super().__init__(*base_args)
        self.health = health
        self.stamina = stamina
        self.base_damage = base_damage
        self.faction = faction
        self.inventory = inventory

    def print_extended(self):
        super().print_extended()
        print(
            f"\tHealth: {self.health}\n" +
            f"\tStamina: {self.stamina}\n" +
            f"\tBase damage: {self.base_damage}\n" +
            f"\tFaction: {self.faction}\n" +
            f"\tInventory: {self.inventory}\n\n"
        )

if __name__ == '__main__':

    test_entity = Entity(
        '&',
        (255, 0, 0),
        'test_entity',
        (-1, -1),
        'A test entity!',
        True
    )
    test_entity.print_extended()

    test_container = Container(
        ['banana', 'screw', 'coin'],
        'jha9d7ya987sdfh',
        'D',
        (0,255,0),
        'test_container',
        (-1,-1),
        'A test container!',
        True
    )
    test_container.print_extended()

    test_mob = Mob(
        100,
        50,
        14,
        'void-walker',
        ['sword of unreality'],
        'X', 
        (0,0,255), 
        'test_mob', 
        (-1,-1),  
        'A test mob!',
        True
    )
    test_mob.print_extended()