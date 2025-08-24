# Problem: Given a string, find the first non-repeated character.
n = input("Enter string: ")
for c in n:
    if n.count(c) == 1:
        print("char is: ", c)
