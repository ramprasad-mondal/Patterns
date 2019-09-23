a = int(input('Enter the no of rows: '))
for row in range(a):
    print('* '*(row+1)+' '*4*(a-row-1)+'* '*(row+1))
for row in range(a,0,-1):
    print('* '*(row)+' '*4*(a-row)+'* '*(row))