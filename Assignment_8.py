# Byrjum á að skilgreina a og b sem 1
# Gerum while lykkju sem runnast endalaust á meðan a er jafnt eða minna en 3
# Síðan notum við if setningar fyrir hvern reit sem að segja hvert má fara og senda leikmanninn síðan á réttan reit
# Þegar leikmaður lendir á 3,1 prentum við Victory! og notum break skipun til að stöðva kóðan

#1,1=north
#1,2=south,east, north
#1,3=south,east
#2,1=north
#2,2=south,west
#2,3=west,east
#3,1=victory
#3,2=north,south
#3,3=south,west

# https://github.com/Hnizer/Forritun

a=1
b=1
while a<=3:
    if a == 1:
        if b == 1:
            print('You can travel: (N)orth.')
            direction=input('Direction: ')
            if direction == 'n' or direction == 'N':
                  b += 1
            else:
                print('Not a valid direction!')
        elif b == 2:
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction=input('Direction: ')
            if direction == 'n' or direction == 'N':
                b += 1
            elif direction == 'e' or direction == 'E':
                a += 1
            elif direction == 's' or direction == 'S':
                b -= 1
            else:
                print('Not a valid direction!')
        elif b == 3:
            print('You can travel: (E)ast or (S)outh.')
            direction=input('Direction: ')
            if direction == 'e' or direction == 'E':
                a += 1
            elif direction == 's' or direction == 'S':
                b -= 1
            else:
                print('Not a valid direction!')
    elif a == 2:
        if b == 1:
            print('You can travel: (N)orth.')
            direction=input('Direction: ')
            if direction == 'n' or direction == 'N':
                  b += 1
            else:
                print('Not a valid direction!')
        elif b == 2:
            print('You can travel: (S)outh or (W)est.')
            direction=input('Direction: ')
            if direction == 's' or direction == 'S':
                b -= 1
            elif direction == 'w' or direction == 'W':
                a -= 1
            else:
                print('Not a valid direction!')
        elif b == 3:
            print('You can travel: (E)ast or (W)est.')
            direction=input('Direction: ')
            if direction == 'e' or direction == 'E':
                a += 1
            elif direction == 'w' or direction == 'W':
                a -= 1
            else:
                print('Not a valid direction!')
    elif a == 3:
        if b == 1:
            print('Victory!')
            break
        elif b == 2:
            print('You can travel: (N)orth or (S)outh.')
            direction=input('Direction: ')
            if direction == 'n' or direction == 'N':
                b += 1
            elif direction == 's' or direction == 'S':
                b -= 1
            else:
                print('Not a valid direction!')
        elif b == 3:
            print('You can travel: (S)outh or (W)est.')
            direction=input('Direction: ')
            if direction == 's' or direction == 'S':
                b -= 1
            elif direction == 'w' or direction == 'W':
                a -= 1
            else:
                print('Not a valid direction!')
