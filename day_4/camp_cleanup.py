
full_overlaps = 0
overlaps = 0
with open( "input", "r" ) as f:
    for l in f.readlines():
        [ start1, stop1 ], [ start2, stop2 ] = [ map( int, x.split('-') ) for x in l.split(',') ]
        if ( start1 >= start2 and stop1 <= stop2 ) or \
           ( start2 >= start1 and stop2 <= stop1 ):
            full_overlaps += 1
        if not ( start1 > stop2 or stop1 < start2 ):
            overlaps += 1
    print( full_overlaps )
    print( overlaps )

# END
