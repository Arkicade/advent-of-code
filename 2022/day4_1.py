def pair_is_contained(pair1, pair2):
    ## we define pairs as an array of two numbers
    ## [lower bound, upperbound]
    ## the conversion is simple as they're defined by
    ## 'lower-upper' in the text file
    return (pair1[0] >= pair2[0] and pair1[1] <= pair2[1]) or (pair2[0] >= pair1[0] and pair2[1] <= pair1[1])

def pair_overlaps(pair1, pair2):
    return (pair2[0] <= pair1[1] and pair2[1] >= pair1[0]) or (pair1[0] <= pair2[1] and pair1[1] >= pair2[0])


def convert_format(pair):
    numpair = pair.split('-')
    ## this doesn't work??
    #for num in numpair:
        #num = int(num)
    numpair = [int(numpair[0]), int(numpair[1])]
    return numpair

with open('camp_sections.txt') as file:
    #PART A
    rangecontains = 0
    for line in file:
        line = line.strip()
        twopairs = line.split(',')
        pair1 = convert_format(twopairs[0])
        pair2 = convert_format(twopairs[1])
        if pair_is_contained(pair1, pair2):
            rangecontains += 1
    print(rangecontains)


with open('camp_sections.txt') as file:
    #PART B
    rangeoverlaps = 0
    for line in file:
        line = line.strip()
        twopairs = line.split(',')
        pair1 = convert_format(twopairs[0])
        pair2 = convert_format(twopairs[1])
        if pair_overlaps(pair1, pair2):
            rangeoverlaps += 1
    print(rangeoverlaps)


