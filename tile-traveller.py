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

def compass(direction):
    if direction == "n":
        y = north(y)
        return y
    if direction == "s":
        y = south(y)
        return y
    if direction == "e":
        x = east(x)
        return x
    if direction == "w":
        x = west(x)
        return x
    



    
def print_north():
    return "(N)orth"
def print_south():
    return "(S)outh"
def print_east():
    return "(E)ast"
def print_west():
    return "(W)est"
    
        

def ui():
    direction = str(input("Direction: "))
    direction = direction.lower()
    return direction



#variables
running = True
position_x = 1
position_y = 1


while running == True:
    direction = ui()
    if direction != "n" and direction != "s" and direction != "e" and direction != "w":
        print("Not a valid directon!")
    position = compass(direction)
    if position_x == 1 and position_y == 1:
        print("You can travel {}".format(print_north()))
    if position_x == 1 and position_y == 2:
        print("You can travel {} or {} or {}.".format(print_north(),print_south(),print_east()))
    if position_x == 1 and position_y == 3:
        print("You can travel {} or {}.".format(print_south(),print_east()))    
    if position_x == 3 and position_y == 1:
        victory()
        running = False
    
    
    

