def findstep(step):
    direction = {'L':[-1,0], 'R':[1,0], 'D':[0,-1], 'U':[0,1]}
    # command = direction[step]
    ## in original bit I computed the WHOLE step, but I realised it's easier to just
    ## break down the steps into singular individual units as opposed to the entire steps
    #for i in range(len(command)):
    #    command[i] = command[i]*unit
    return direction[step]

def check_step(head, tail):
    hor_diff = head[0] - tail[0]
    ver_diff = head[1] - tail[1]
    if abs(hor_diff) <= 1 and abs(ver_diff) <= 1:
        return [head, tail]
    elif abs(hor_diff) == 2 and ver_diff == 0:
        tail = add_coords(tail, [hor_diff//2,0])
    elif abs(ver_diff) == 2 and hor_diff == 0:
        tail = add_coords(tail, [0, ver_diff//2])
    else:
        target = [round_up(hor_diff), round_up(ver_diff)]
        tail = add_coords(tail, target)
    return [head, tail]
    

""" def check1_twostep(head, tail):
    hor_diff = head[0] - tail[0]
    ver_diff = head[1] - tail[1]
    if hor_diff == 0 and ver_diff != 0:
        return [0,ver_diff]
    elif ver_diff == 0 and hor_diff != 0:
        return [hor_diff, 0]
    else:
        check2_notouch()

def check2_notouch():
    return False

def movestep():
    return 0 """

def add_coords(coord1, coord2):
    new_coords = [coord1[0]+coord2[0], coord1[1]+coord2[1]]
    return new_coords

def round_up(num):
    if abs(num) == 1:
        return num
    else:
        return num//2

with open('rope_bridge.txt') as file:
    hpos = [0,0]
    tpos = [0,0]
    locations_visited = []
    print_limit = 20
    for line in file:
        line = line.strip()
        [direction, unit] = line.split(" ")
        unit = int(unit)
        #print(findstep(direction, unit))
        command = findstep(direction)
        while unit > 0:
            if tpos not in locations_visited:
                locations_visited.append(tpos)
            hpos = add_coords(hpos, command)
            [hpos, tpos] = check_step(hpos, tpos)
            #if print_limit > 0:
            #    print("HPOS")
            #    print(hpos)
            #    print("TPOS")
            #    print(tpos)
            #    print_limit -=1
            unit -= 1
    print(len(locations_visited))

