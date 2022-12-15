from colour_printer import fg, bg, util


class Tile:
    '''A representation of a single tile.'''
    def __init__(self, symbol, colour, name, position, occupiable, damage, description=''):
        self.symbol = symbol
        self.colour = colour # (R, G, B)
        self.name = name
        self.position = position # (row, column)
        self.occupiable = occupiable
        self.damage = damage
        self.description = description
        self.occupying_entity = None
        
    def __str__(self):
        if self.occupying_entity:
            return (
                f"{fg.rgb(self.occupying_entity.colour[0], self.occupying_entity.colour[1], self.occupying_entity.colour[2])}" + 
                f"{self.occupying_entity.symbol}{util.RESET}"
            )
        else:
            return (
                f"{fg.rgb(self.colour[0], self.colour[1], self.colour[2])}" + 
                f"{self.symbol}{util.RESET}"
            )

    def clone(self, position):
        '''Returns new instances of tile with same attributes in new position.'''
        return Tile(
            self.symbol,
            self.colour,
            self.name,
            position, # Must be given new position as tuple.
            self.occupiable,
            self.damage,
            self.description
        )
        
    def print_extended(self):
        '''Intended for displaying tilesets and in-game descriptions of tiles.'''
        print(
            f"\t\t{self}\n" + 
            f"\t{self.name}\n" + 
            f"\toccupiable: {self.occupiable}\n" + 
            f"\tDPT: {self.damage}\n" + 
            f"\tDescription:\n\t\t{self.description}\n"
        )

    def occupy(self, entity):
        if not self.occupying_entity:
            self.occupying_entity = entity
            self.occupiable = False
            return True
        else: return False


class TileSet:
    '''Representation of all the tile-kinds in the game. Tiles are added to and parsed from a text file.'''
    def __init__(self, filename):
        self.tiles = []
        self.filename = filename
        with open(self.filename, 'r') as tile_file:
            for line in tile_file:
                if line != '\n' and line.split()[0] != '//': # Allows for blank lines in tile files for readability.
                    line = line.split('|')
                    tile = Tile(
                        line[0],
                        tuple(map(int, line[1].split(','))),
                        line[2],
                        (-1, -1), # Since these are template tiles, position should be invalid.
                        True if line[3] == 'True' else False,
                        int(line[4]),
                        line[5]
                    )
                    self.tiles.append(tile)

    def print_set(self):
        '''Displays the properties of all tiles in the current loaded tileset.'''
        print(f"\n\tTileSet: {self.filename.split('_')[0]}\n")
        for tile in self.tiles:
            tile.print_extended()

    def add_tile(self, tile):
        '''Appends new Tile data to tileset file.'''
        duplicate = False
        with open(self.filename, 'r') as tile_file:  
            for line in tile_file:
                if tile.name == line.split('|')[2]:
                    duplicate = True
            if not duplicate:
                with open(self.filename, 'a') as tile_file:
                    line = (
                        f"\n{tile.symbol}|" +
                        f"{','.join(list(map(lambda v: str(v), tile.colour)))}|" +
                        f"{tile.name}|" +
                        f"{tile.ground}|" +
                        f"{tile.damage}|" +
                        f"{tile.description}"
                    )
                    tile_file.write(line)
                    print(f"{fg.GREEN}{tile.name} successfully added to {self.filename}!{util.RESET}")
            else:
                print(f'{fg.RED}Cannot add tile {tile.name}; already in loaded tileset!{util.RESET}')


if __name__ == '__main__':

    tileset = TileSet(".\\resources\\default_tiles.txt")
    tileset.print_set()

