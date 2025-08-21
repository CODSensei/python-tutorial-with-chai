# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
color = input("Enter fruit color: ")
status = {
    "green": "Unripe",
    "yellow": "Ripe",
    "brown": "Overripe",
}
if color.lower() in status:
    print(f"Fruit is {status[color.lower()]}")
else:
    print("Fruit color is invalid!!")
