grade = int(input("What is your test score: "))

if grade < 60:
    print("Grade F")
elif 60 <= grade <= 69:
    print("Grade D")
elif 70 <= grade <= 79:
    print("Grade C")
elif 80 <= grade <= 89:
    print("Grade B")
elif 90 <= grade <= 100:
    print("Grade A")
else:
    print("Please enter a valid input")
