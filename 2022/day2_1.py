def scoreperline_ver1(line):
    score = 0
    opponent = line[0]
    response = line[2]
    # X = rock, Y = paper, Z = scissors
    item_score = {'X':1, 'Y':2, 'Z':3}
    score += item_score[response]
    ## first dictionary corresponds to if opponent is A: or rock
    ## second dict is for B: paper
    ## third dict is for C: scissors
    battle_score = [{'X':3, 'Y':6, 'Z':0},{'X':0, 'Y':3, 'Z':6},{'X':6, 'Y':0, 'Z':3}]
    if opponent == 'A':
        getdict = battle_score[0]
    elif opponent == 'B':
        getdict = battle_score[1]
    elif opponent == 'C':
        getdict = battle_score[2]

    score += getdict[response]
    return score


def scoreperline_ver2(line):
    score = 0
    opponent = line[0]
    strategy = line[2]
    # X = lose, Y = draw, Z = win
    battle_score = {'X':0, 'Y':3, 'Z':6}
    score += battle_score[strategy]
    ## first dictionary corresponds to if opponent is A: or rock
    ## second dict is for B: paper
    ## third dict is for C: scissors
    battle_score = [{'X':3, 'Y':1, 'Z':2},{'X':1, 'Y':2, 'Z':3},{'X':2, 'Y':3, 'Z':1}]
    if opponent == 'A':
        getdict = battle_score[0]
    elif opponent == 'B':
        getdict = battle_score[1]
    elif opponent == 'C':
        getdict = battle_score[2]
    score += getdict[strategy]
    return score

def totalscore_ver1(lines):
    score = 0
    for line in lines:
        score += scoreperline_ver1(line)
    return score


def totalscore_ver2(lines):
    score = 0
    for line in lines:
        score += scoreperline_ver2(line)
    return score


with open('rps_strategy.txt') as file:
    #print(totalscore_ver1(file))
    print(totalscore_ver2(file))