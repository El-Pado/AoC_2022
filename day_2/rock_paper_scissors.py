
rock     = 1
paper    = 2
scissors = 3

winning = {
        rock:paper,
        paper:scissors,
        scissors:rock,
        }

shape = {
        'A':rock,
        'B':paper,
        'C':scissors,
        'X':rock,
        'Y':paper,
        'Z':scissors,
        }

score = 0
with open( "input", "r" ) as f:
    for him, me in [ x.split() for x in f.readlines() ]:
        him, me = shape[him], shape[me]
        score += me
        if him == me:
            score += 3
        elif me == winning[him]:
            score += 6
    print( score )

lose = 0
draw = 3
win  = 6

outcome = {
        'X':lose,
        'Y':draw,
        'Z':win,
        }

score = 0
with open( "input", "r" ) as f:
    for him, end in [ x.split() for x in f.readlines() ]:
        him, end = shape[him], outcome[end]
        score += end
        if end == draw:
            score += him
        elif end == win:
            score += winning[him]
        else:
            score += ( 6 - him - winning[him] )
    print( score )

# END
