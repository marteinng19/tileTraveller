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

    if position_x == 1 and position_y == 1:
        print("You can travel: {}.".format(print_north()))
        direction = ui()
        if direction != "n":
            print("Not a valid direction!")
        elif direction == "n":
            position_y = north(position_y)

    if position_x == 1 and position_y == 2:
        print("You can travel: {} or {} or {}.".format(print_north(),print_east(),print_south()))
        direction = ui()
        if direction != "n" and direction != "s" and direction != "e":
            print("Not a valid direction!")
        elif direction == "n":
            position_y = north(position_y)
        elif direction == "s":
            position_y = south(position_y)
        elif direction == "e":
            position_x = east(position_x)
    
    if position_x == 1 and position_y == 3:
        print("You can travel: {} or {}.".format(print_east(),print_south())) 
        direction = ui()
        if direction != "s" and direction != "e":
            print("Not a valid direction!")
        elif direction == "s":
            position_y = south(position_y)
        elif direction == "e":
            position_x = east(position_x)

    if position_x == 2 and position_y == 1:
        print("You can travel: {}.".format(print_north()))
        direction = ui()
        if direction != "n":
            print("Not a valid direction!")
        elif direction == "n":
            position_y = north(position_y)

    if position_x == 2 and position_y == 2:
        print("You can travel: {} or {}.".format(print_south(),print_west()))
        direction = ui()
        if direction != "w" and direction != "s":
            print("Not a valid direction!")
        elif direction == "w":
            position_x = west(position_x)
        elif direction == "s":
            position_y = south(position_y)

    if position_x == 2 and position_y == 3:
        print("You can travel: {} or {}.".format(print_east(),print_west()))
        direction = ui()
        if direction != "e" and direction != "w":
            print("Not a valid direction!")
        elif direction == "w":
            position_x = west(position_x)
        elif direction == "e":
            position_x = east(position_x)

    if position_x == 3 and position_y == 3:
        print("You can travel: {} or {}.".format(print_south(),print_west()))
        direction = ui()
        if direction != "s" and direction != "w":
            print("Not a valid direction!")
        elif direction == "s":
            position_y = south(position_y)
        elif direction == "w":
            position_x = west(position_x)

    if position_x == 3 and position_y == 2:
        print("You can travel: {} or {}.".format(print_north(),print_south()))
        direction = ui()
        if direction != "n" and direction != "s":
            print("Not a valid direction!")
        elif direction == "s":
            position_y = south(position_y)
        elif direction == "n":
            position_y = north(position_y)

    if position_x == 3 and position_y == 1:
        victory()
        running = False
    
    
    

