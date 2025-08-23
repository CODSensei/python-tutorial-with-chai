# Problem: Reverse a string using a loop.
original = input("Enter string: ")
reverse = ""
for c in original:
    reverse = c + reverse
print("reverse: ", reverse)
