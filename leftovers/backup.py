import itertools

n_zombies = 2 # number of zombies
l_bridge = 5 # length of the bridge
positions = [2, 3] # positions of zombies in the bridge [1...l_bridge]

zombies = dict() # the dict that stores the current state of zombies
lowest_step = 9999999999999 # variable to store lowest step
highest_step = 0 # variable to store highest step

step = 0 # temp variable to count steps

def move_one_step():
    flip_zombies_direction()

    for k, v in zombies.items():
        # move left, v[1] = direction, v[0] = position
        if v[1] == 0:
            zombies[k] = [v[0]-1, v[1]]
        # move right, v[1] = direction, v[0] = position
        elif v[1] == 1:
            zombies[k] = [v[0]+1, v[1]]
    
    print(zombies)
    remove_crossed_zombies()
    

def remove_crossed_zombies():
    to_be_delete = []

    for k, v in zombies.items():
        if v[0] <= 0 or v[0] >= l_bridge + 1:
            to_be_delete.append(k)
    
    for k in to_be_delete:
        del zombies[k]


def search_for_flipping_candidate():
    occupied_positions = dict() # storing POSITION as key, value is [INDEX, DIRECTION]
    colliders = [] # storing index of face to face zombies (a.k.a going to collide soon)
    overlappers = [] # storing index of overlapped zombies (a.k.a occupy the same position)

    for k, v in zombies.items():
        if v[0] in occupied_positions:
            # there is already a zombie in this position
            overlappers.append(occupied_positions[v[0]][0])
            overlappers.append(k)
        else:
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

    return overlappers, colliders


def flip_zombies_direction():
    overlappers, colliders = search_for_flipping_candidate()

    #print(colliders)
    # flip direction
    for k in overlappers:
        flip(k)

    for k in colliders:
        flip(k)


def flip(k):
    # flip right to left
    if zombies[k][1] == 1:
        zombies[k][1] = 0
    # flip left to right
    elif zombies[k][1] == 0:
        zombies[k][1] = 1

'''
def search_overlapped_zombies():
    occupied_positions = dict() # storing position by index
    overlapped_index = [] # stroing index of overlapped zombies

    for k, v in zombies.items():
        # there is a zombie in this position
        if v[0] in occupied_positions:
            overlapped_index.append(occupied_positions[v[0]]) # index of stored zombie
            overlapped_index.append(k) # index of current zombie
        else:
            occupied_positions[v[0]] = k

    return overlapped_index

def flip_zombies_direction():
    # check if two zombies occupy the same position
    overlappers = search_overlapped_zombies()

    print("overlappers")
    print(overlappers)

    for k in overlappers:
        # flip right to left
        if zombies[k][1] == 1:
            zombies[k][1] = 0
        # flip left to right
        elif zombies[k][1] == 0:
            zombies[k][1] = 1

    # check if zombie are face to face
'''

# generate a sequence of all possible walking direction for all zombies
direction_seq = [''.join(i) for i in itertools.product('01', repeat=n_zombies)]

for directions in direction_seq:
    print("#################### begin sequence ####################")
    # initialize the zombies
    for i in range(n_zombies):
        zombies[i] = [int(positions[i]), int(directions[i])]
        
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