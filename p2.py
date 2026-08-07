n = int(input("Enter total expected numbers : "))
roll = list(map(int, input("Enter the numbers with one missing number: ").split()))
total = (n * (n + 1)) // 2
s = sum(roll)
print("missing number is", total - s)
