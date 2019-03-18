import itertools

n_zombies = 2 # number of zombies
l_bridge = 5 # length of the bridge
positions = [2, 3] # positions of zombies in the bridge [1...l_bridge]

zombies = [] # the list that stores the current state of zombies
lowest_step = 9999999999999 # variable to store lowest step
highest_step = 0 # variable to store highest step

step = 0 # temp variable to count steps

def move_one_step():
    for zombie in zombies:
        # move left
        if zombie["direction"] == 0:
            zombie["position"] -= 1
        # move right
        elif zombie["direction"] == 1:
            zombie["position"] += 1
    
    print(zombies)
    
    #flip_zombies_direction()
    remove_crossed_zombies()

    # check if zombie are overlap
    # check if zombie are face to face

def remove_crossed_zombies():
    to_be_delete = []
    for zombie in zombies:
        if zombie["position"] <= 0 or zombie["position"] >= l_bridge + 1:
            to_be_delete.append(zombie["index"])
    
    to_be_delete.sort(reverse=True)
    for i in to_be_delete:
        if zombie
        zombies.pop(i)

def search_overlapped_zombies():
    occupied_positions = dict() # storing position by index
    overlapped_index = [] # stroing index of overlapped zombies
    for zombie in zombies:
        # there is a zombie in this position
        if zombie["position"] in occupied_positions:
            overlapped_index.append(occupied_positions[zombie["position"]]) # return index
            overlapped_index.append(zombie["index"])
        else:
            occupied_positions[zombie["position"]] = zombie["index"]

    return overlapped_index

def flip_zombies_direction():
    overlappers = search_overlapped_zombies()
    for overlap in overlappers:
        # flip right to left
        if zombies[int(overlap)]["direction"] == 1:
            zombies[int(overlap)]["direction"] = 0
        # flip left to right
        elif zombies[int(overlap)]["direction"] == 0:
            zombies[int(overlap)]["direction"] = 1
        #print(zombies[int(overlap)])

# generate a sequence of all possible walking direction for all zombies
direction_seq = [''.join(i) for i in itertools.product('01', repeat=n_zombies)]

for directions in direction_seq:
    print("#################### begin sequence ####################")
    # initialize the zombies
    for i in range(n_zombies):
        zombie = dict()
        zombie["index"] = i
        zombie["position"] = int(positions[i])
        zombie["direction"] = int(directions[i])
        zombies.append(zombie)
        
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