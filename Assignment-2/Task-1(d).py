# Task-1(d)

counter = 18

while counter <= 63:

    if counter == 63:
        print(-1 * counter)
    elif counter % 2 == 0:
        print(counter, end = ', ')
    else:
        print(-1 * counter, end = ', ')

    counter = counter + 9

#OR:
#for i in range(18, 63, 9):

#    if i % 2 == 0:
#        print(i, end = ', ')
#    else:
#        print( -1 * i, end = ', ')

#print(-63)
