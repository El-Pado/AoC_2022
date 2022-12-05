
import copy

stacks = []
stacks_v2 = []
end_of_conf = False
with open( "input", "r" ) as f:
    for l in f.readlines():
        if l.strip() == '' or l[1] == '1':
            end_of_conf = True
            stacks_v2 = copy.deepcopy( stacks )
        elif end_of_conf == False:
            for i in range(len(l)//4):
                if len(stacks) <= i:
                    stacks.append( [] )
                if l[4*i+1] != ' ':
                    stacks[i].insert( 0, l[4*i+1] )
        else:
            nb_crates, start, end = [ int(x) for x in l.strip().split(' ') if x.isdigit() ]
            for i in range( nb_crates-1, -1, -1 ):
                stacks[end-1].append( stacks[start-1][-1] )
                stacks[start-1].pop(-1)
                stacks_v2[end-1].append( stacks_v2[start-1][-1-i] )
                stacks_v2[start-1].pop(-1-i)

    top_crates = ''.join( [ stacks[i][-1] for i in range(len(stacks)) ] )
    print( top_crates )
    top_crates_v2 = ''.join( [ stacks_v2[i][-1] for i in range(len(stacks_v2)) ] )
    print( top_crates_v2 )

# END
