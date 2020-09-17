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
    return running
#def encode_direction(compass):
#    if compass == n:

#values
running = True
position = 11
user_input = str(input("Direction: "))

direction = user_input.lower()

while running == True:

    if direction == "n":
        north(position)
        print(position)
    if direction == "s":
        south(position)
        print(position)
    if direction == "e":
        east(position)
        print(position)
    if direction == "w":
        west(position)
        print(position)
    if position == 31:
        victory()

