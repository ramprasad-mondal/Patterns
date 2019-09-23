a = int (input("Enter the no: "))
for row in range(a):
    for col in range(a):
        if(col<=row):
            print("*", end=' ')
    print()