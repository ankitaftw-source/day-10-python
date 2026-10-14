num = int(input("Enter the number of lines you need :"))
s = 1
for i in range(0,num):
    for j in range(0,i+1):
        print(s,end=" ")
        s = s+1
    print()