a = int (input('enter the no: '))

for row in range(a):
    for col in range(a):
        if (col==0 or col==int(a-1) or row==0 or row==int(a-1)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()