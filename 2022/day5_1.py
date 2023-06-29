def make_stack(lines):
    stacks_list = [[],[],[],[],[],[],[],[],[]]
    i = 1
    for x in lines:
        if i < 9:
            j = 0
            full_line = [(x[i:i+4]) for i in range(0, len(x), 4)]
            while j < 9:
                l = full_line[j]
                letter  = "".join([ch for ch in l if ch.isalpha()])
                stacks_list[j].append(letter)
                j += 1
        else:
            break
        i += 1
    return stacks_list

def convert_stack(blocks):
    stack = []
    i = len(blocks)-1
    while i >= 0:
        if blocks[i] != '':
            stack.append(blocks[i])
        i -= 1
    return stack

def convert_command(line):
    keywords = line.split(' ')
    numaction = int(keywords[1])
    pickup = int(keywords[3])-1
    drop = int(keywords[5])-1
    return [numaction, pickup, drop]

def move_block(stacks, pickup,drop):
    block = stacks[pickup].pop()
    stacks[drop].append(block)

def move_blocks(stacks, numblocks, pickup, drop):
    blocks = []
    for i in range(numblocks):
        bloc = stacks[pickup].pop()
        blocks.append(bloc)
    for j in range(len(blocks)):
        bloc = blocks.pop()
        stacks[drop].append(bloc)

def topblock(stacks):
    for i in range(len(stacks)):
        print(stacks[i].pop(),end ="")

#### preparing the various stacks
f=open('crates.txt',"r")
lines=f.readlines()
stacks_list = make_stack(lines)
for i in range(9):
    stacks_list[i] = convert_stack(stacks_list[i])
f.close()


with open('crates.txt') as file:
    counter = 0
    for line in file:
        if counter > 9:
            line = line.strip()
            cmd = convert_command(line)
            # PART B
            move_blocks(stacks_list, cmd[0], cmd[1], cmd[2])
            # PART A
            #for i in range(cmd[0]):
                #move_block(stacks_list, cmd[1],cmd[2])
        counter += 1
    print(stacks_list)
    topblock(stacks_list)

   
    
    