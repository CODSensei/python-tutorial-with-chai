# Problem: Check if a number is prime.
n = int(input("Enter number: "))

c = 0
for i in range(2, n):
    if n % i == 0:
        c = 1
        break
if c == 1:
    print("Not prime")
else:
    print("Prime")
