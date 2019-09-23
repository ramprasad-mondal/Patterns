a = int(input('Enter the no of rows: '))
b=1
for row in range(a):
    for col in range(a-row):
        print(' ',end=' ')
    for col in range(row+1):
        print(b,end=' ')
        b=b+1
    b=1
    for col in range(row):
        print(row,end=' ')
        row=row-1
    print()