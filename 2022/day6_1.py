def start_marker(n, line):
    l = 0
    u = n
    isrepeating = True
    while u < len(line) and isrepeating:
        chunk = line[l:u]
        isrepeating = (len(set(chunk)) != len(chunk))
        if isrepeating:
            l += 1
            u += 1
    if isrepeating:
        return 0
    else:
        return u




with open('databuffer.txt') as file:
    for line in file:
        print(start_marker(4,line))
        ## for part B replace 4 with "14"