a = int(input('Enter the no of rows: '))
b=0
for row in range(a):
    for col in range(a-row):
        print(' ',end=' ')
    for col in range(row+1):
        print(chr(ord('A')+b),end=' ')
        b=b+1
    b=0
    for col in range(row):
        print(chr(ord('A')+row-1),end=' ')
        row=row-1
    print()