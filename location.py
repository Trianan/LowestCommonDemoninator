import tiles
from PIL import Image

import os

tileset = tiles.Tileset('.\\resources\\default_tiles.txt')

class Location:
    def __init__(self, map_file):
        self.name = map_file.split('.')[0]
        print(f'Location: {self.name}')
        self.map_tiles = []

        with Image.open(map_file, 'r') as map_data:
            width, height = map_data.size
            os.system(f'mode con:cols={width + 8}')

            rgb_values = list(map_data.getdata())
            for i in range(height):
                row = []
                for j in range(width):
                    rgb_value = rgb_values.pop(0)
                    for tile in tileset.tiles:
                        if rgb_value == tile.colour:
                            row.append(tile.clone())
                self.map_tiles.append(row)
            
    def __str__(self):
        rows = ""
        for row in self.map_tiles:
            r = []
            for t in row:
                r.append(str(t))
            rows += '\n' + ''.join(r)
        return rows

if __name__ == '__main__':
    test_map = Location('Test Map', '.\\locations\\test_map.png')
    print(test_map)