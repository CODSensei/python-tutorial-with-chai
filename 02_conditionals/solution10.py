# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
species = input("Enter the species: ").lower()
age = int(input("Enter pet's age: "))

if species == "dog" and age < 2:
    print("Puppy food")
elif species == "cat" and age > 5:
    print("Senior Cat food")
else:
    print("Invalid inputs!!")
