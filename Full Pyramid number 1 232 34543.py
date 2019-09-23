a = int(input('Enter the no of rows: '))
b=1
for row in range(a):
    b = row+1
    for col in range(a-row):
        print(' ',end=' ')
    for col in range(row+1):
        print(b, end=' ')
        b=b+1
    b=b-2
    for col in range(row):
        print(b, end=' ')
        b=b-1
    #b=b+2  # or we can write "b=row+1" after the row for loop
    print()