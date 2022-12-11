from colour_printer import fg, bg, util

class Tile:
    '''A representation of a single tile.'''
    def __init__(self, symbol, colour, name, is_ground, damage, description=''):
        self.symbol = symbol
        self.colour = colour # (R, G, B)
        self.name = name
        self.ground = is_ground
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



    def clone(self):
        '''Returns new instances of tile with same attributes.'''
        return Tile(
            self.symbol,
            self.colour,
            self.name,
            self.ground,
            self.damage,
            self.description
        )
        
    def print_extended(self):
        print(  f"\t\t{self}\n" + 
                f"\t{self.name}\n" + 
                f"\tis_ground: {self.ground}\n" + 
                f"\tDPT: {self.damage}\n" + 
                f"\tDescription:\n\t\t{self.description}\n")

class Tileset:
    '''Representation of all the tiles in the game. Tiles are added to and parsed from a text file.'''
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
                        True if line[3] == 'True' else False,
                        int(line[4]),
                        line[5]
                    )
                    self.tiles.append(tile)

    def print_set(self):
        print(f"\n\tTileset: {self.filename.split('_')[0]}\n")
        for tile in self.tiles:
            tile.print_extended()

    def add_tile(self, tile):
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
                    self.tiles.append(tile)
                    print(f"{fg.GREEN}{tile.name} successfully added to {self.filename}!{util.RESET}")
            else:
                print(f'{fg.RED}Cannot add tile {tile.name}; already in loaded tileset!{util.RESET}')

if __name__ == '__main__':

    tileset = Tileset(".\\resources\\default_tiles.txt")
    tileset.print_set()

