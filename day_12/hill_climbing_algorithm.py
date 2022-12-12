
S = (0,0)
E = (0,0)
heightmap = {}
map_h = 0
map_w = 0
with open( "input", "r" ) as f:
    for i, l in enumerate( map( lambda x: x.strip(), f.readlines() ) ):
        for j, h in enumerate( l ):
            if h == 'S':
                S = (i,j)
                h = 'a'
            if h == 'E':
                E = (i,j)
                h = 'z'
            heightmap[(i,j)] = h
            map_h = i
            map_w = j


def elevation( dest, source ):
    return ord( heightmap[dest] ) - ord( heightmap[source] )

def add_pos( pos ):
    if not pos in visited_pos:
        visited_pos.append( pos )
        new_pos.append( pos )

def get_shortest_path( start_pos ):
    global visited_pos
    global new_pos
    min_path_len = len( heightmap )
    for index, s in enumerate( start_pos ):
        #print( "Testing start position " + str(index+1) + "/" + str(len(start_pos)) )
        visited_pos = [s]
        new_pos = [s]
        path_len = 0
        while not E in visited_pos:
            path_len += 1
            # Optim 1
            if path_len >= min_path_len:
                break
            # Optim 2
            if len(start_pos) > 1 and not [s] == new_pos:
                new_pos = [ pos for pos in new_pos if heightmap[pos] != heightmap[s] ]
            for i, j in new_pos.copy():
                if i < map_h and elevation( (i+1,j), (i,j) ) <= 1:
                    add_pos( (i+1,j) )
                if i > 0 and elevation( (i-1,j), (i,j) ) <= 1:
                    add_pos( (i-1,j) )
                if j < map_w and elevation( (i,j+1), (i,j) ) <= 1:
                    add_pos( (i,j+1) )
                if j > 0 and elevation( (i,j-1), (i,j) ) <= 1:
                    add_pos( (i,j-1) )
                new_pos.pop( 0 )
        min_path_len = min( path_len, min_path_len )
    return min_path_len

print( get_shortest_path( [S] ) )
print( get_shortest_path( [pos for pos,h in heightmap.items() if h == 'a'] ) )

# END
