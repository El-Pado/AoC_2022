
scan = set()
lowest = 0
with open( "input", "r" ) as f:
    for i, l in enumerate( map( lambda x: x.strip(), f.readlines() ) ):
        p1 = l.split(' -> ')[0]
        for p2 in l.split(' -> ')[1:]:
            i1,j1 = eval( p1 )
            i2,j2 = eval( p2 )
            if i1 == i2:
                for j in range( min(j1,j2), max(j1,j2)+1 ):
                    scan.add( (i1,j) )
                    lowest = max( lowest, j )
            elif j1 == j2:
                lowest = max( lowest, j1 )
                for i in range( min(i1,i2), max(i1,i2)+1 ):
                    scan.add( (i,j1) )
            p1 = p2


def move_sand():
    global sand, nb_sands
    i,j = sand
    if j < lowest:
        if (i,j+1) in scan:
            if (i-1,j+1) in scan:
                if (i+1,j+1) in scan:
                    scan.add( (i,j) )
                    nb_sands += 1
                else:
                    sand = (i+1,j+1)
                    move_sand()
            else:
                sand = (i-1,j+1)
                move_sand()
        else:
            sand = (i,j+1)
            move_sand()


init_scan = scan.copy()
source = (500,0)
sand = (0,0)
nb_sands = 0

while sand[1] < lowest:
    sand = source
    move_sand()
print( nb_sands )


scan = init_scan.copy()
floor = lowest + 2
lowest = floor + 1
nb_sands = 0

for i in range( source[0]-floor, source[0]+floor+1 ):
    scan.add( (i,floor) )

while sand != source:
    sand = source
    move_sand()
print( nb_sands )

# END
