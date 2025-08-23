# Problem: Calculate the sum of even numbers up to a given number n.
n = int(input("Enter number: "))
sum = 0
for i in range(n + 1):
    if i % 2 == 0:
        sum += i
print("Sum: ", sum)
