# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
def greet(a="User"):
    print(f"Hello {a}")


a = input("Enter you name: ")
greet(a)
greet()
