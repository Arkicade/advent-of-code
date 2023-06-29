def cleanline(line):
    newline = ''.join(i for i in line if i.isdigit())
    return newline


def makearray(lines):
    arr = [0]
    i = 0
    for line in lines:
        if line == "\n":
            arr.append(0)
            i += 1
        else:
            l = cleanline(line)
            arr[i] = arr[i] + int(l)

    return arr

def elfcalorie(cals):
    cals = makearray(cals)
    return max(cals)


def top3(cals):
    cals = makearray(cals)
    top1 = max(cals)
    cals.remove(top1)
    top2 = max(cals)
    cals.remove(top2)
    top3 = max(cals)
    totalsum = sum([top1, top2, top3])
    return totalsum


#file_path = '/Users/datagy/Desktop/sample_text.txt'

with open('calories.txt') as file:
    print(top3(file))