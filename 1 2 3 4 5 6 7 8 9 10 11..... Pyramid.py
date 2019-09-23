a = int(input('Enter the number of rows: '))
b=1
for row in range(a):
    for col in range(row+1):
        print(b, end=' ')
        b=b+1
    print()