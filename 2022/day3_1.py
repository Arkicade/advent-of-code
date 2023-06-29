### USE SETS !!!! 

def overlap_item(comp_1, comp_2):
    item = ''
    for c1 in comp_1:
        for c2 in comp_2:
            if c1 == c2: item = c1
    return item

def total_overlaps(sack_1, sack_2):
    items = []
    for c1 in sack_1:
        for c2 in sack_2:
            if c1 == c2: items.append(c1)
    ##only add if index of first instance of item in items match
    items = [items[i] for i in range(len(items)) if i == items.index(items[i]) ]
    return items

## convert both sack_1 and sack_2 into sets
## and do intersection as python has a builtin function for that

def calculate_value(char):
    char_val = 0
    if char.islower():
        char_val = ord(char) - 96
    else:
        char_val = ord(char) - 38
    return char_val

def line_priority(line):
    m = int(len(line)/2)
    comp_1 = line[:m]
    comp_2 = line[m:]
    shareditem = overlap_item(comp_1, comp_2)
    return calculate_value(shareditem)

def group_priority(line):
    overlapping = total_overlaps(line[0],line[1])
    overlapping = ''.join(overlapping) 
    trueoverlap = total_overlaps(overlapping, line[2])
    return calculate_value(trueoverlap[0])

with open('rucksack.txt') as file:
    #PART A
    totalsum = 0
    for line in file:
        totalsum += line_priority(line.strip())
    print(totalsum)

with open('rucksack.txt') as file:
    # PART B
    groupsum = 0
    i = 1
    groupsacks = []
    for line in file:
        groupsacks.append(line.strip())
        if i%3 == 0:
            groupsum += group_priority(groupsacks)
            groupsacks.clear()
        i += 1
    print(groupsum)


    