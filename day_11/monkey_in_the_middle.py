
import copy
import numpy

init_items = []
operation = []
test = []
if_true = []
if_false = []
with open( "input", "r" ) as f:
    for l in map( lambda x: x.strip(), f.readlines() ):
        if l.startswith( 'Starting items' ):
            init_items.append( list( map( lambda x: int(x.strip()), l.split(':')[-1].split(',') ) ) )
        elif l.startswith( 'Operation' ):
            operation.append( l.split('=')[-1] )
        elif l.startswith( 'Test' ):
            test.append( int(l.split()[-1]) )
        elif l.startswith( 'If true' ):
            if_true.append( int(l.split()[-1]) )
        elif l.startswith( 'If false' ):
            if_false.append( int(l.split()[-1]) )

def run_rounds( nb_rounds, d ):
    items = copy.deepcopy( init_items )
    inspections = [0]*len(items)
    for _ in range( nb_rounds ):
        for m, items_list in enumerate( items ):
            for item in items_list.copy():
                old = item
                item = ( eval( operation[m] ) // d ) % numpy.prod( test )
                inspections[m] += 1
                if item % test[m] == 0:
                    items[if_true[m]].append( item )
                else:
                    items[if_false[m]].append( item )
                items[m].pop(0)
    return inspections

print( numpy.prod( sorted( run_rounds(   20, 3) )[-2:] ) )
print( numpy.prod( sorted( run_rounds(10000, 1) )[-2:] ) )

# END
