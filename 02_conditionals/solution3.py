# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).
score = int(input("Enter student score: "))
if score < 60:
    print("Grade - F")
elif score < 70:
    print("Grade - D")
elif score < 80:
    print("Grade - C")
elif score < 90:
    print("Grade - B")
elif score <= 100:
    print("Grade - A")
else:
    print("Invalid Score!!")
