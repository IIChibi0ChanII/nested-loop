num = int(input("enter a number: "))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

for i in range(1, num+1):
    for j in range(1, num+1):
        print("*", end=" ")
    print()

for ro in range(1, num+1):
    for co in range(1, ro+1):
        print("*", end=" ")
    print()

l = num

for row in range(1, num+1):
    for col in range(num,l-num,-1):
        l += 1
        print("*", end=" ")
    print()