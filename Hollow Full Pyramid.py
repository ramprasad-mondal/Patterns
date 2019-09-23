a = int(input('Enter the no of row: '))
for row in range(a):
    for col in range(row):
        print(end=' ')
    for col in range(a):
        if(row==0 or col==0 or row+col==a-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
