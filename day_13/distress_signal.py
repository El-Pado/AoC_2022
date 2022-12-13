
import copy

pairs = [[]]
with open( "input", "r" ) as f:
    for i, l in enumerate( map( lambda x: x.strip(), f.readlines() ) ):
        if l == '':
            pairs.append([])
        else:
            pairs[-1].append(eval(l))


def compare( l, r ):
    #print("Comparing", l, "and", r)
    res = None
    if isinstance( l, int ) and isinstance( r, int ):
        if l < r:
            res = True
        elif l > r:
            res = False
    elif isinstance( l, list ) and isinstance( r, list ):
        while res == None and not ( not l and not r ):
            if r and not l:
                res = True
            elif l and not r:
                res = False
            else:
                res = compare( l[0], r[0] )
                l.pop(0)
                r.pop(0)
    elif isinstance( l, int ):
        res = compare( [l], r )
    else:
        res = compare( l, [r] )
    return res

def condition( element ):
    return element["order"]

def order( packets ):
    for i, packet in enumerate( packets ):
        for other_packet in packets[i+1:]:
            if compare( copy.deepcopy( packet["packet"] ), copy.deepcopy( other_packet["packet"] ) ):
                other_packet["order"] += 1
            else:
                packet["order"] += 1


right_order = []
for i, [l, r] in enumerate( copy.deepcopy( pairs ) ):
    if compare( l, r ):
         #print("--> Right order for pair", i+1)
        right_order.append( i+1 )
print( sum( right_order ) )


packets = [ {"packet":[[2]],"order":0},
            {"packet":[[6]],"order":0} ]
for [l, r] in pairs:
    packets.append( {"packet":l,"order":0} )
    packets.append( {"packet":r,"order":0} )
order( packets )
packets.sort( key = condition )

decoder_key = 1
for i, packet in enumerate( packets ):
    if packet["packet"] in ( [[2]], [[6]] ):
        decoder_key *= i+1
print( decoder_key )

# END
