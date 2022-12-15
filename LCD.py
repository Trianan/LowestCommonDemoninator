import os
import keyboard

from colour_printer import fg, bg, util 
from location import Location

class Game:
    def __init__(self, map_file, entities_file, tileset, entityset):
        self.location = Location(
            map_file,
            entities_file,
            tileset, # optional
            entityset # optional
        )

    def play(self):
        playing = True
        while playing:

            os.system('cls')
            print(self.location)

            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                match event.name:
                    case 'esc':
                        playing = False

        print(f'{fg.RED}Game terminated.{util.RESET}')

game = Game('test_map.png', 'test_entities.png')
game.play()