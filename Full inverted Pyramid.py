a = int(input('Enter the no of rows: '))
for row in range(a):
    for col in range(row):
        print(end=' ')
    for col in range(a-row):
        print('*', end=' ')
    print()