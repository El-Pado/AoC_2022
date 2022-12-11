
H = [0,0]
T = [0,0]
K = [ [0]*2 for i in range(9) ]
tail_positions_1 = [tuple(T)]
tail_positions_2 = [tuple(K[-1])]

def update_knot( h, t ):
    if abs(h[0]-t[0]) == 2:
        t[0] += (h[0]-t[0])//2
        if h[1] != t[1]:
            t[1] += (h[1]-t[1])//abs(h[1]-t[1])
    elif abs(h[1]-t[1]) == 2:
        t[1] += (h[1]-t[1])//2
        if h[0] != t[0]:
            t[0] += (h[0]-t[0])//abs(h[0]-t[0])

with open( "input", "r" ) as f:
    for l in map( lambda x: x.strip(), f.readlines() ):
        d, n = l.split()
        for i in range(int(n)):
            if d == 'U':
                H[0] -= 1
            elif d == 'D':
                H[0] += 1
            elif d == 'L':
                H[1] -= 1
            elif d == 'R':
                H[1] += 1
            update_knot( H, T )
            update_knot( H, K[0] )
            for i in range( 1, len( K ) ):
                update_knot( K[i-1], K[i] )
            tail_positions_1.append( tuple(T) )
            tail_positions_2.append( tuple(K[-1]) )

print( len( set( tail_positions_1 ) ) )
print( len( set( tail_positions_2 ) ) )

# END
