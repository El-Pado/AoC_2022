
list_calories = []
nb_tot_cal = 0
with open( "input", "r" ) as f:
    for nb_calories in f.readlines():
        try:
            nb_tot_cal += int( nb_calories )
        except:
            list_calories.append( nb_tot_cal )
            nb_tot_cal = 0
print( max( list_calories ) )

nb_tops = 3
top_n = 0
for i in range( nb_tops ):
    top = max( list_calories )
    list_calories.remove ( top )
    top_n += top
print( top_n )

# END
