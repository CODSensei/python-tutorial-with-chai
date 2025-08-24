# Problem: Keep asking the user for input until they enter a number between 1 and 10.
n = int(input("Enter number: "))
while n < 1 or n > 10:
    n = int(input("Re-Enter the number: "))
    if n >= 1 and n <= 10:
        break
