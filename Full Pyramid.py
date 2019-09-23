a = int(input('Enter the number of rows: '))
for row in range(a):
    for col in range(a-1-row):
        print(end=' ')
    for col in range(row+1):
        print('*', end=' ')
    print()