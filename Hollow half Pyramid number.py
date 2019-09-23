a = int(input('Enter the no of rows: '))
for row in range(a):
    for col in range(a):
        if(row==a-1 or col==0 or row==col):
            print(col+1, end=' ')
        else:
            print(' ', end=' ')
    print()