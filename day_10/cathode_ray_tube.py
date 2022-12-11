
def sig_strength(i):
    return cycles[i]*i

x = 1
cycles = []
with open( "input", "r" ) as f:
    for l in map( lambda x: x.strip(), f.readlines() ):
        instr = l.split()[0]
        if instr == 'noop':
            cycles.append(x)
        elif instr == 'addx':
            cycles.append(x)
            cycles.append(x)
            x += int( l.split()[1] )
print( sum( sig_strength(i) for i in [20,60,100,140,180,220] ) )

crt = []
for i in range( len( cycles ) ):
    if i % 40 == 0:
        crt.append('')
    if i % 40 in range( cycles[i]-1, cycles[i]+2 ):
        crt[-1] += '#'
    else:
        crt[-1] += '.'
for line in crt:
    print(line)

# END
