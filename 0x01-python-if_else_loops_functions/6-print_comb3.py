#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        print('{:d}{:d}'.format(x,y), end='')
        if x != 9 and y != 9:
            print(', ', end='')
print()
