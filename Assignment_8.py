# Byrjum á því að skilgreina hvern reit
# Gerum while lykkju sem endar þegar við förum á 3,1

#1,1=north
#1,2=south,east, north
#1,3=south,east
#2,1=north
#2,2=south,west
#2,3=west,east
#3,1=victory
#3,2=north,south
#3,3=south,west

a=1
b=1
while a != 3 and b != 1:
    if a == 1:
        if b == 1:
            stefna='(N)orth'
        elif b == 2:
            stefna='(N)orth or (E)ast or (S)outh'
        elif b == 3:
            stefna='(E)ast or (S)outh'
    elif a == 2:
        if b == 1:
            stefna='(N)orth'
        elif b == 2:
            stefna='(S)outh or (W)est'
        elif b == 3:
            stefna='(E)ast or (W)est'
    elif a == 3:
        if b == 1:
            print('Victory!')
            break
        elif b == 2:
            stefna='(N)orth or (S)outh'
        elif b == 3:
            stefna='(S)outh or (W)est'
    print('You can travel: {}.'.format(stefna))
    direction=input('Direction: ')
    if direction == 'n' or direction == 'N':
        b += 1
    elif direction == 'e' or direction == 'E':
        a += 1
    elif direction == 's' or direction == 'S':
        b -= 1
    elif direction == 'w' or direction == 'W':
        a -= 1
    else:
        print('Not a valid direction!')
            
            
