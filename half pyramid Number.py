a = int(input('Enter the number of rows: '))
for row in range(a):
    for col in range(row+1):
        print(col+1, end=' ')
    print()