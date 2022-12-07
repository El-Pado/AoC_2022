
# Note: tree and cur_dir finally have no use in this puzzle, as no on files and files tree is required
tree = {}
cur_dir = tree
path_dir = []
size_dir = {}
with open( "input", "r" ) as f:
    for l in map( lambda x: x.strip(), f.readlines() ):
        if l.startswith( '$ cd ' ):
            if l.split(' ')[-1] == '..':
                cur_dir = tree
                for direc in path_dir[:-1]:
                    cur_dir = cur_dir[direc]
                path_dir.pop(-1)
            else:
                size_dir[ '/'.join(path_dir + [l.split(' ')[-1]]) ] = 0
                cur_dir[ l.split(' ')[-1] ] = {}
                cur_dir = cur_dir[ l.split(' ')[-1] ]
                path_dir.append( l.split(' ')[-1] )
        elif l.startswith( 'dir ' ):
            pass
            cur_dir[ l.split(' ')[-1] ] = {}
        elif l.split(' ')[0].isdigit():
            cur_dir[ l.split(' ')[-1] ] = l.split(' ')[0]
            size_dir[ '/'.join(path_dir) ] += int(l.split(' ')[0])
            for i in range(1,len(path_dir)):
                size_dir[ '/'.join(path_dir[:-i]) ] += int(l.split(' ')[0])

print( sum( [ size_dir[path] for path in size_dir if size_dir[path] <= 100000 ] ) )
print( min( size for path, size in size_dir.items() if size >= 30000000-(70000000-size_dir['/']) ) )

# END
