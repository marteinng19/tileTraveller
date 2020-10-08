import random as rand
# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
YES = 'y'
NO = 'n'
LEVERS = [(1,2), (2,2), (2,3), (3,2)]


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
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions


def pull_lever(is_lever, total_coins):
    if is_lever:
        lever = rand.choice([YES, NO])
        print("Pull a lever (y/n):", lever)

    if lever == "y":
        total_coins = total_coins + 1
        print("You received 1 coin, your total is now {}.".format(total_coins))
        return 1
    elif lever == "n": 
        return 0


def play_one_move(col, row, valid_directions):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = rand.choice([NORTH, EAST, SOUTH, WEST])
    print("Direction:", direction)

    if not direction in valid_directions:
        print("Not a valid direction!")
        valid = False
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        valid = True
    return victory, col, row, valid

def check_if_lever(col, row,):
    for i in LEVERS:
        if col == i[0] and row == i[1]:
            return True

# The main program starts here
play_again = ""
while play_again.lower() != "n":
    victory = False
    row = 1
    col = 1
    rand.seed(int(input("Input seed: ")))
    total_coins = 0
    moves = 0
    while not victory:

        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, valid = play_one_move(col, row, valid_directions)
        is_lever = check_if_lever(col, row)
        if is_lever:
            if valid:
                new_value = pull_lever(is_lever, total_coins)
                total_coins += new_value
        moves += 1
    print("Victory! Total coins {}. Moves {}.".format(total_coins, moves))
    play_again = input("Play again (y/n): ")