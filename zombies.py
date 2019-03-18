import itertools

# inputs
N_ZOMBIES = 3 # number of zombies
L_BRIDGE = 5 # length of the bridge
POSITIONS = [2, 3, 4] # positions of zombies in the bridge [1...L_BRIDGE]

# the dict that stores the current state of zombies
# key is ZOMBIE_ID (int) value is [POSITION (int), DIRECTION (int)]
# POSITION is from 1 to L_BRIDGE
# DIRECTION is 0 for LEFT and 1 for RIGHT
zombies = dict()

# the dict to store the info whether the zombie already moved
# key is ZOMBIE_ID (int) value is MOVED (bool)
# MOVED is set default to False, set to True when it use it chance to move
zombies_moved = dict()

lowest_step = 9999999999999 # variable to store lowest step
highest_step = 0 # variable to store highest step
step = 0 # temp variable to count steps

def move_one_step():
    # move to the next position is considered as one move
    # flip direction is considered as one move

    # set move to false
    for k in zombies_moved:
        zombies_moved[k] = False

    flip_zombies_direction()

    for k, v in zombies.items():
        if zombies_moved[k] == False:
            # the zombie has not moved yet
            if v[1] == 0:
                # move left
                zombies[k] = [v[0]-1, v[1]]
            elif v[1] == 1:
                # move right
                zombies[k] = [v[0]+1, v[1]]
            
            zombies_moved[k] = True
    
    print(zombies)
    remove_crossed_zombies()
    

def remove_crossed_zombies():
    to_be_delete = []

    for k, v in zombies.items():
        if v[0] <= 0 or v[0] >= L_BRIDGE + 1:
            to_be_delete.append(k)
    
    for k in to_be_delete:
        del zombies[k]


def search_for_flipping_candidate():
    occupied_positions = dict() # storing POSITION as key, value is [INDEX, DIRECTION]
    colliders = [] # storing index of face to face zombies (a.k.a going to collide soon)

    for k, v in zombies.items():
        # convert the zombies dict to the new position key format
        occupied_positions[v[0]] = [k, v[1]]

    for k, v in occupied_positions.items():
        if v[1] == 1:
            # move right
            try:
                if occupied_positions[k+1][1] == 0:
                    # check if there is zombies on its right facing left
                    colliders.append(occupied_positions[k+1][0]) # zombie id for right neighbor
                    colliders.append(v[0]) # zombie id for this position
            except KeyError as error:
                pass # no zombie on the right side

    return colliders


def flip_zombies_direction():
    colliders = search_for_flipping_candidate()

    for k in colliders:
        flip(k)


def flip(k):
    # flip right to left
    if zombies[k][1] == 1:
        zombies[k][1] = 0
    # flip left to right
    elif zombies[k][1] == 0:
        zombies[k][1] = 1

    # flip is considered as one move
    zombies_moved[k] = True


# generate a sequence of all possible walking direction for all zombies
direction_seq = [''.join(i) for i in itertools.product('01', repeat=N_ZOMBIES)]

for directions in direction_seq:
    print("#################### begin sequence ####################")
    # initialize the zombies
    for i in range(N_ZOMBIES):
        zombies[i] = [int(POSITIONS[i]), int(directions[i])]
        zombies_moved[i] = False
        
    print(zombies)
    # do the movement until all the zombies go out of the bridge
    print("-------------------- begin moving --------------------")
    while len(zombies) > 0:
        step += 1
        move_one_step()

    print("# steps = " + str(step))

    # check if the steps might be the lowest or the highest
    if step < lowest_step:
        lowest_step = step
    elif step > highest_step:
        highest_step = step

    # reset all the things
    step = 0
    zombies.clear()

print("#################### Result ####################")
print("lowest steps = " + str(lowest_step))
print("highest steps = " + str(highest_step))