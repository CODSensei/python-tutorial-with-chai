# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]


items = ["apple", "banana", "orange", "apple", "mango"]
unique_set = set()

for item in items:
    if item in unique_set:
        print("duplicate: ", item)
        break
    unique_set.add(item)
