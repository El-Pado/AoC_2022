
import re

sensors = {}
with open( "input", "r" ) as f:
    for l in map( lambda x: x.strip(), f.readlines() ):
        x1 = int( re.split( r'[=,:]', l)[1]  )
        y1 = int( re.split( r'[=,:]', l)[3]  )
        x2 = int( re.split( r'[=,:]', l)[-3] )
        y2 = int( re.split( r'[=,:]', l)[-1] )
        sensors[(x1,y1)] = (x2,y2)


def dist( a, b ):
    return abs( a[0] - b[0] ) + abs( a[1] - b[1] )

def get_no_beacon_nb( row ):
    no_beacon = set()
    for sensor, beacon in sensors.items():
        dist_b = dist( sensor, beacon )
        dist_r = dist( sensor, (sensor[0], row) )
        if dist_b >= dist_r:
            delta = dist_b - dist_r
            for x in range( sensor[0]-delta, sensor[0]+delta+1 ):
                if (x,row) != beacon:
                    no_beacon.add( x )
    return no_beacon

def find_hidden_beacon( xy_min, xy_max ):
    for y in range( xy_min, xy_max+1 ):
        #if y%1000 == 0: print("Row " + str(y) + "/" + str(xy_max) )
        x = xy_min
        no_beacon = True
        while no_beacon and x <= xy_max:
            for sensor, beacon in sensors.items():
                if dist( sensor, beacon ) >= dist( sensor, (x,y) ):
                    no_beacon = False
                    x = sensor[0] + dist( sensor, beacon ) - dist( sensor, (sensor[0],y) ) + 1
                    break
            if no_beacon:
                return (x,y)
            no_beacon = True


print( len( get_no_beacon_nb( 2000000 ) ) )

distress_beacon = find_hidden_beacon( 0, 4000000 )
print( 4000000 * distress_beacon[0] + distress_beacon[1] )

# END
