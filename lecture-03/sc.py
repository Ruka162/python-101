
score_1 = float(input("Enter the first score: "))
score_2 = float(input("Enter the second score: "))
score_3 = float(input("Enter the third score: "))
average_score = (score_1 + score_2 + score_3) / 3
print(f"the average_score is: {average_score}")
if average_score > 95:
    print("congratulations")
    print("you have a high average score")
    