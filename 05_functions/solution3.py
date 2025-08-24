# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
def multi(a, b):
    return a * b


c = int(input("Press 1) two numbers or 2) one number and one string: "))
if c == 1:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
else:
    a = input("Enter a: ")
    b = int(input("Enter b: "))

print(multi(a, b))
