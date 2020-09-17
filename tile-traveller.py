#functions
def north(tile):
    tile += 1
    return tile
def south(tile):
    tile -= 1
    return tile

def east(tile):
    tile += 10
    return tile

def west(tile):
    tile -= 10
    return tile

#values
running = True
position = 11


while running:
    
    if direction == n or N:
        north(position)
    if direction == s or S:
        south(position)
    if direction == e or E:
        east(position)
    if direction == w or W:
        west(position)
    if tile == 31:
        running = False


print("Victory!")