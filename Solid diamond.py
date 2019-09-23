a = int(input('Enter the no of rows: '))
for row in range(a):
    print(' '*(a-row-1)+'* '*(row+1))
for row in range(a,0,-1):
    print(' '*(a-row)+'* '*(row))