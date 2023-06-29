def check_direction(dir, row, col, lines):
    ## for part B
    sight_distance = 0
    ## dir will be an array of two elements[dirWE, dirNS]
    dirWE = dir[0]
    dirNS = dir[1]
    ## dirWE is -1 if checking WEST (for an edge to the west)
    ## dirWE is +1 if checking EAST
    ## dirNS is -1 if checking SOUTH
    ## dirNS is +1 if checking NORTH
    ## we ONE of these directions (will be called over in a loop)
    tree_height = lines[row][col]
    i = dirWE
    j = dirNS

    while (row+j) >= 0 and (row+j) < len(lines)  and (col+i) >= 0 and (col+i) < len(lines[0]):
        ###LINE of sight in the direction WE or NS
        sight_distance += 1
        los = lines[row+j][col+i]
        if row == 7 and col == 51:
            print("--------------")
            print(row+j)
            print(col+i)
            print("--- NUMBER ---")
            print(los)
        if los >= tree_height:
            ## means you CANNOT see the tree
            return False, sight_distance
        i += dirWE
        j += dirNS
    return True, sight_distance


def scenic_score(alldirs):
    result = 1
    for dir in alldirs:
        result = result * dir
    return result


## maybe way to save informaiton
## if you keep track of a tree1 being "visible" in one way (say EAST)
## ALL trees east to it, can't be visible by WEST (as we know tree1 is WEST and is larger)


with open('trees.txt') as file:
    dirs = [[1,0],[-1,0],[0,1],[0,-1]] 
    lines=file.readlines()
    visible_trees = 0
    scenic_tree = 0
    ## clearing \n from lines
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        for j in range(len(lines[i])):
            check_visibility = False
            scenic_dirs = []
            for dir in dirs:
                [is_visible, distance_score] = check_direction(dir, i, j, lines)
                if is_visible and check_visibility == False:
                    visible_trees += 1
                    check_visibility = True
                if i == 7 and j == 51:
                    print("### CHECKING DISTANCE ###")
                    print(dir)
                    print(distance_score)
                scenic_dirs.append(distance_score)
            score = scenic_score(scenic_dirs)
            if score > scenic_tree:
                scenic_tree = score
    ### PART A
    print(visible_trees)
    ### PART B
    print(scenic_tree)

    
