# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math


def circle(r):
    area = math.pi * r * r
    circumference = 2 * math.pi * r

    return area, circumference


n = int(input("Enter radius: "))
a, c = circle(n)
print("Area: ", a, "circumference: ", c)
print(circle(n))
