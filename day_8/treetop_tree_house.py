

trees = []
with open( "input", "r" ) as f:
    for l in map( lambda x: x.strip(), f.readlines() ):
        trees.append( list( map( int, l ) ) )

visible_trees = []
for i in range( len( trees ) ):
    for j in range( len( trees[i] ) ):
        if 0 in (i,j) or j == len( trees[i] )-1 or i == len( trees[j] )-1:
            visible_trees.append( (i,j) )
        else:
            if max( trees[i][:j] ) < trees[i][j] or max( trees[i][j+1:] ) < trees[i][j] or \
               max( x[j] for x in trees[:i] ) < trees[i][j] or max( x[j] for x in trees[i+1:] ) < trees[i][j]:
                visible_trees.append( (i,j) )
print( len( set( visible_trees ) ) )


scenic_scores = []
for i in range( len( trees ) ):
    for j in range( len( trees[i] ) ):
        if 0 in (i,j) or j == len( trees[i] )-1 or i == len( trees[j] )-1:
            scenic_scores.append( 0 )
        else:
            scenic_scores.append( 1 )
            for k in range(1,j+1):
                if trees[i][j-k] >= trees[i][j] or k == j:
                    scenic_scores[-1] *= k
                    break
            for k in range(1,i+1):
                if trees[i-k][j] >= trees[i][j] or k == i:
                    scenic_scores[-1] *= k
                    break
            for k in range(1,len(trees[i])-j):
                if trees[i][j+k] >= trees[i][j] or k == len(trees[i])-j-1:
                    scenic_scores[-1] *= k
                    break
            for k in range(1,len(trees)-i):
                if trees[i+k][j] >= trees[i][j] or k == len(trees)-i-1:
                    scenic_scores[-1] *= k
                    break
print( max( scenic_scores ) )

# END
