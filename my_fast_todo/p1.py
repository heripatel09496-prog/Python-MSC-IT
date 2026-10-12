n = int(input("Enter number of elements: "))

a = list(map(int, input("Enter numbers: ").split()))

for i in range(len(a) - 1):

    if a[i] == a[i+1]:
      
        if i == 0 or a[i] != a[i-1]:
            print(a[i])
