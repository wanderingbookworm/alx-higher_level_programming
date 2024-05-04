#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x + 1, 10):
        print('{:02d}'.format(x), end='')
        print('{:02d}'.format(y), end='')
        if x != 8 and y != 9:
            print(', ', end='')
print()
