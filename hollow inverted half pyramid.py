a = int(input("Enter the no: "))
for row in range(a):
    for col in range(a):
        if (col==0 or row==0 or row+col==a-1):
            print('*', end=' ')
        else:
                print(' ', end=' ')
    print()