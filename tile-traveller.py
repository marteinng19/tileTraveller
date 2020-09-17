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
def victory():
    running = False
    print("Victory!")

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
    if position == 31:
        victory()

