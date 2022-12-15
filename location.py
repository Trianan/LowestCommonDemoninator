import tile as tl
import entity as ent

from PIL import Image
from datetime import datetime
import os


class Location:
    def __init__(self, map_file, entities_file, tileset='default_tiles', entityset='default_entities'):
        self.name = ' '.join(list(map(lambda s: s.title(), map_file.split('\\')[-1].split('.')[0].split('_'))))
        self.tileset = tl.TileSet(f'.\\resources\\{tileset}.txt')
        self.entityset = ent.EntitySet(f'.\\resources\\{entityset}.txt')
        self.tiles = []
        self.entities = []

        # These next two blocks can be refactored with the image reading being one function:
        with Image.open(map_file, 'r') as map_data:
            self.width, self.height = map_data.size
            rgb_values = list(map_data.getdata())
            for i in range(self.height):
                row = []
                for j in range(self.width):
                    rgb_value = rgb_values.pop(0)[0:3] # [0:3] deals with RGBA values sometimes read by getdata().
                    for tile in self.tileset.tiles:
                        if rgb_value == tile.colour: 
                            row.append(tile.clone((i, j))) # Each tile is given their coordinates here.
                self.tiles.append(row)
        
        with Image.open(entities_file, 'r') as entity_data:
            w, h = entity_data.size
            if (w, h) == (self.width, self.height):
                rgb_values = list(entity_data.getdata())
                for i in range(self.height):
                    row = []
                    for j in range(self.width):
                        rgb_value = rgb_values.pop(0)[0:3]
                        for entity in self.entityset.entities:
                            if rgb_value == entity.colour:
                                spawned_entity = entity.clone((i, j))
                                row.append(spawned_entity)
                                self.tiles[i][j].occupy(spawned_entity) # This is how entities are displayed.
                    self.entities.append(row)
            else:
                print("Invalid entity file: dimensions don't match map file!.")

        os.system(f'mode con:cols={self.width * 2} lines={self.height * 2}')

    def __str__(self):
        rows = ""
        for row in self.tiles:
            r = []
            for t in row:
                r.append(str(t))
            rows += '\n' + ''.join(r)
        return rows + f'\nLOCATION: {self.name}\tSIZE: {self.width}x{self.height} tiles.\n'


if __name__ == '__main__':

    def continue_debug():
        yn = input('\nRun next test? (y/n): ')
        os.system('cls')
        return True if yn == 'y' else False

    print('\n\tMAP DRAW:\n')
    test_map = Location('.\\mapdata\\test_map.png', '.\\mapdata\\test_entities.png')
    print(test_map)

    if continue_debug():
        for row in test_map.entities:
            for entity in row:
                entity.print_extended()
                print(f'Position: {entity.position}')

    if continue_debug():
        print('\n\tMAP2 DRAW:\n')
        test_map2 = Location('.\\mapdata\\test_map_large.png', '.\\mapdata\\test_entities_large.png')
        print(test_map2)

    if continue_debug():
        print('\n\tTILE COORDINATES:\n')
        logging = True if input('Write coordinates to log file? (y/n): ') == 'y' else False
        log_filename = f".\\logs\\{'_'.join(test_map.name.lower().split())}_coords.txt"
        log_file = open(log_filename, 'w') if logging else 'Not currently logging.'
        if logging: log_file.write(f"'{test_map.name}' COORDINATES LOG - (Created at: {datetime.now()})\n\n")

        for row in test_map.tiles:
            for tile in row:
                line = (
                    f"Tile: {tile.name} | " +
                    f"Occupant: {tile.occupying_entity} | " +
                    f"Position: ({tile.position[0]}, {tile.position[1]})"
                )
                if logging:
                    log_file.write(line + '\n')
                else:
                    print(line)
        if logging:
            log_file.close()