a = int(input("Enter the no: "))
for row in range(a):
    for col in range(a):
        if(row<=col):
            print("*", end=' ')
    print()