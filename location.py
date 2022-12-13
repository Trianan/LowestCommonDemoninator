import tiles

from PIL import Image
from datetime import datetime
import os

tileset = tiles.TileSet('.\\resources\\default_tiles.txt')

class Location:
    def __init__(self, map_file, entity_file):
        self.name = ' '.join(list(map(lambda s: s.title(), map_file.split('\\')[-1].split('.')[0].split('_'))))
        self.map_tiles = []
        self.map_entities = []

        with Image.open(map_file, 'r') as map_data:
            self.width, self.height = map_data.size
            os.system(f'mode con:cols={self.width + 8}')

            rgb_values = list(map_data.getdata())
            for i in range(self.height):
                row = []
                for j in range(self.width):
                    rgb_value = rgb_values.pop(0)
                    for tile in tileset.tiles:
                        if rgb_value == tile.colour:
                            row.append(tile.clone((i, j))) # Each tile is given their coordinates here.
                self.map_tiles.append(row)

        #with Image.open(entity_file, 'r') as entity_data:


            
    def __str__(self):
        rows = ""
        for row in self.map_tiles:
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
    test_map = Location(
        '.\\mapdata\\test_map.png',
        '.\\mapdata\\test_entities.png'
    )
    print(test_map)
    
    if continue_debug():
        print('\n\tTILE COORDINATES:\n')
        logging = True if input('Write coordinates to log file? (y/n): ') == 'y' else False
        log_filename = f".\\logs\\{'_'.join(test_map.name.lower().split())}_coords.txt"
        log_file = open(log_filename, 'w') if logging else 'Not currently logging.'
        if logging: log_file.write(f"'{test_map.name}' COORDINATES LOG - (Created at: {datetime.now()})\n\n")

        for row in test_map.map_tiles:
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