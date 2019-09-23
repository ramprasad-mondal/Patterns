a= int(input('Enter the no of rows: '))
for row in range(a):
    for col in range(a-row):
        print(end=' ')
    for col in range(a):
        if(col==0 or row==col):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

for row in range(a):
    for col in range(row+2):
        print(end=' ')
    for col in range(a-1-row):
        if(col==0 or row+col==a-2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()