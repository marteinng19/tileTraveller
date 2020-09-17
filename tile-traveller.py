#functions
def north(pos):
    pos += 1
    return pos

def south(pos):
    pos -= 1
    return pos

def east(pos):
    pos += 1
    return pos

def west(pos):
    pos -= 1
    return pos

def victory():
    running = False
    print("Victory!")
    return running

def print_pos():
    print(position_x,position_y)

def ui():
    direction = str(input("Direction: "))
    direction = direction.lower()
    return direction



#values
running = True
position_x = 1
position_y = 1


while running == True:
    direction = ui()
    if direction != "n" and direction != "s" and direction != "e" and direction != "w":
        print("Not a valid directon!")
    if direction == "n":
        position_y = north(position_y)
        print_pos()
    if direction == "s":
        position_y = south(position_y)
        print_pos()
    if direction == "e":
        position_x = east(position_x)
        print_pos()
    if direction == "w":
        position_x = west(position_x)
        print_pos()
    if position_x == 3 and position_y == 1:
        victory()
        running = False
    
    

