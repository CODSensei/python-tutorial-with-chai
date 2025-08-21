# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.
size = input("Change order size to: ").lower()
extra = input("Do you want extra shot of expresso? ")

if extra == "yes":
    if size == "small":
        print("change order size to small with extra shot of expresso")
    elif size == "medium":
        print("change order size to medium with extra shot of expresso")
    elif size == "large":
        print("change order size to large with extra shot of expresso")
    else:
        print("Invalid value")
if extra == "no":
    if size == "small":
        print("change order size to small")
    elif size == "medium":
        print("change order size to medium")
    elif size == "large":
        print("change order size to large")
    else:
        print("Invalid value")
