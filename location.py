import tiles
tileset = tiles.Tileset('default_tiles.txt')

class Location:
    def __init__(self, name, filename):
        self.name = name
        self.local_tiles = []
        with open(filename, 'r') as location_data:
            for line in location_data:
                line = list(map(lambda t: t.strip(), line.split('|')))
                tile_line = []
                for tilename in line:
                    for tile in tileset.tiles:
                        if tilename == tile.name:
                            tile_line.append(tile.clone())
                self.local_tiles.append(tile_line)

    def __str__(self):
        rows = []
        for raw_row in self.local_tiles:
            row = '\n' + ''.join(list(map(lambda t: str(t), raw_row)))
            rows.append(row)
        return ''.join(rows)

def blank_location(name, tile, size):
    with open(f".\\locations\\{name}.txt", 'a') as new_location:
        location = []
        for i in range(size[0]):
            row = []
            for j in range(size[1]):
                row.append(f'{tile.name}')
            row = '|'.join(row)
            location.append(row)
        location = '\n'.join(location)
        new_location.write(location)
    return Location(name, f'.\\locations\\{name}.txt')

def insert_structure(structure_file, insert_at):






    
    return

if __name__ == '__main__':
    test_map = Location('Test Map', '.\\locations\\test_level.txt')
    print(test_map)

    lvl_1 = blank_location('level_1', tileset.tiles[1], (32, 96))
    print(lvl_1)