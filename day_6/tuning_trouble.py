
with open( "input", "r" ) as f:
    signal = f.readline().strip()
    i = 0
    while len(signal[i:i+4]) != len(set(signal[i:i+4])):
        i += 1
    end_of_marker = i+4
    print( end_of_marker )
    i = 0
    while len(signal[i:i+14]) != len(set(signal[i:i+14])):
        i += 1
    end_of_marker = i+14
    print( end_of_marker )

# END
