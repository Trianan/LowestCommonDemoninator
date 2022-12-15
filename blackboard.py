import keyboard
import os

player = '$'
x, y = 0, 0
print(f'Starting at: (x: {x}, y: {y})')

grid_size = 10
test_grid = []
for r in range(grid_size):
    row = []
    for c in range(grid_size):
        row.append('.')
    test_grid.append(row)
test_grid[y][x] = player
print(*test_grid, sep='\n')

def pretty(grid):
    pretty_grid = ''
    for row in grid:
        pretty_grid += (''.join(row) + '\n')
    return pretty_grid

playing = True
while playing:
    os.system('cls')
    print(pretty(test_grid))
    print(f'Currently at: (x: {x}, y: {y})')
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        test_grid[y][x] = '.'
        match event.name:
            # Movement:
            case 'w' | 'up':
                if y > 0:
                    y -= 1
            case 's' | 'down':
                if y < grid_size - 1:
                    y += 1
            case 'd' | 'right':
                if x < grid_size - 1:
                    x += 1
            case 'a' | 'left':
                if x > 0:
                    x -= 1
            case 'esc':
                playing = False
            case _:
                print(f"Unknown key '{event.name}' pressed.\nPress space to continue...")
                keyboard.wait('space')
        test_grid[y][x] = player

class Test:
    def __init__(self):
        self.a = 1
        self.b = 2

x = Test()
print(vars(x))
    

print('Finished.')