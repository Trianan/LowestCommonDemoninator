from colour_printer import fg, bg, util

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
        self.position = position # (row, column)
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
        self.base_traits = tuple(base_args)
        self.inventory = inventory
        self.key = key
        self.locked = True if key else False

    def clone(self, position=(0,0)):
        '''Returns new instances of entity with same attributes.'''
        new_container =  Container(
            self.inventory,
            self.key,
            *self.base_traits
        )
        new_container.position = position
        return new_container

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
        self.base_traits = tuple(base_args)
        self.health = health
        self.stamina = stamina
        self.base_damage = base_damage
        self.faction = faction
        self.inventory = inventory

    def clone(self, position=(0,0)):
        '''Returns new instances of entity with same attributes.'''
        new_mob = Mob(
            self.health,
            self.stamina,
            self.base_damage,
            self.faction,
            self.inventory,
            *self.base_traits
        )
        new_mob.position = position
        return new_mob

    def print_extended(self):
        super().print_extended()
        print(
            f"\tHealth: {self.health}\n" +
            f"\tStamina: {self.stamina}\n" +
            f"\tBase damage: {self.base_damage}\n" +
            f"\tFaction: {self.faction}\n" +
            f"\tInventory: {self.inventory}\n\n"
        )

class EntitySet:
    '''Representation of all entities in the game.'''
    def __init__(self, filename):
        self.entities = []
        self.filename = filename
        with open(self.filename, 'r') as entity_file:
            for line in entity_file:
                if line != '\n' and line.split()[0] != '//': # Allows for blank lines in tile files for readability.
                    line = line.split('|')
                    entity = None
                    match line[0]:
                        case 'E':
                            entity = Entity(
                                line[1],
                                tuple(map(int, line[2].split(','))),
                                line[3],
                                (-1,-1),
                                line[5],
                                True if line[4] == 'True' else False
                            )
                        case 'C':
                            entity = Container(
                                [],
                                '',
                                line[1],
                                tuple(map(int, line[2].split(','))),
                                line[3],
                                (-1,-1),
                                line[5],
                                True if line[4] == 'True' else False
                            )
                        case 'M':
                            entity = Mob(
                                (line[5],)*2, # Health and stamina are stored as...
                                (line[6],)*2, # ... tuples of (current, max).
                                line[7],
                                line[4],
                                [],
                                line[1],
                                tuple(map(int, line[2].split(','))),
                                line[3],
                                (-1,-1),
                                line[9],
                                True if line[8] == 'True' else False
                            )
                    self.entities.append(entity)


if __name__ == '__main__':

    entity_set = EntitySet('.\\resources\\default_entities.txt')
    for entity in entity_set.entities:
        entity.print_extended()