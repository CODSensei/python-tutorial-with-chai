# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
age = int(input("Enter age: "))
day = input("Enter day: ")

price = 12 if age >= 18 else 8
if day.lower() == "wednesday":
    price -= 2

print("Price is: ", price)
