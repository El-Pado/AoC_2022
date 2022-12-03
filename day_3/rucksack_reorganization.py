
priorities = 0
with open( "input", "r" ) as f:
    for l in f.readlines():
        for item in l[:len(l)/2]:
            if item in l[len(l)/2:]:
                break
        if item.islower():
            priorities += ord(item) - ord('a') + 1
        else:
            priorities += ord(item) - ord('A') + 27
    print( priorities )

priorities = 0
items = []
with open( "input", "r" ) as f:
    for i, l in enumerate( f.readlines() ):
        if i%3 == 0:
            items = list(l.strip())
        else:
            items = [ x for x in l if x in items ]
        if i%3 == 2:
            item = items[0]
            if item.islower():
                priorities += ord(item) - ord('a') + 1
            else:
                priorities += ord(item) - ord('A') + 27
    print( priorities )

# END
