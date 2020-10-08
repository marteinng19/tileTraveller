# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
        lever = False
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
        lever = True
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
        lever = False
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
        lever = False
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
        lever = True
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
        lever = True
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
        lever = True
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
        lever = False
    return valid_directions, lever

def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = input("Direction: ")
    direction = direction.lower()
    right_direction = True
    
    if not direction in valid_directions:
        print("Not a valid direction!")
        right_direction = False
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
    return victory, col, row, right_direction

def pull_lever(is_lever, total_coins):
    
    lever = input("Pull a lever (y/n): ")
    lever = lever.lower()

    if lever == "y":
        total_coins = total_coins + 1
        print("You received 1 coin, your total is now {}.".format(total_coins))
        return 1
    elif lever == "n": 
        return 0
def reset():
    col = 1
    row = 1
    total_coins = 0
    victory = False

    return col, row, total_coins, victory
# The main program starts here
victory = False
row = 1
col = 1
total_coins = 0
play_again = ""

while play_again != "n":
    if play_again == "y":
        col, row, total_coins, victory = reset()
    while not victory:
        valid_directions, is_lever = find_directions(col, row)
        if is_lever and right_direction:
            new_value = pull_lever(is_lever, total_coins)
            total_coins += new_value
        print_directions(valid_directions)
        victory, col, row, right_direction = play_one_move(col, row, valid_directions)

    print("Victory! Total coins {}.".format(total_coins))
    play_again = input("Play again? (y/n): ")