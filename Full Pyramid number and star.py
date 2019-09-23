a = int(input('Enter the number of rows: '))
for row in range(a):
    for col in range(a-row):
        print(end='*')
    for col in range(row+1):
        print(row+1, end='*')
    for col in range(a-row-1):
        print(end='*')
    print()