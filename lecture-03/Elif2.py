score = int(input("Enter score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
elif score <= 49:
    print("Grade: F")
else:
    print("Grade: D or F")