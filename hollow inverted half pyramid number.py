a = int(input('Enter the no of rows: '))
for row in range(a):
    for col in range(a):
        if(row==0 or col==0 or row+col==a-1):
            print(col+1,end=' ')
        else:
            print(' ', end=' ')
    print()