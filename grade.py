# User marks input
marks = float(input("enter your marks (0-100): "))

# Grading Logic
if marks >= 90 and marks <= 100:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
elif marks < 50 and marks >= 0:
    grade = "Fail"
else:
    grade = "Invalid Input! Please enter marks between 0 and 100."

# Result print karna
print(f"your Grade is: {grade}")
