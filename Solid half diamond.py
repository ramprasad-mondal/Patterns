a = int(input('Enter the no of rows: '))
for row in range(a):
    print('* '*(row+1))
for row in range(a-1,0,-1):
    print('* '*(row))