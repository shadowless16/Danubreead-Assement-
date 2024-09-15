age = int(input("How hold are you: "))
driving_license = input("Do you have a driving license? Y/N \n").lower()

if age >= 18 and driving_license == "yes":
    print ("You are allowed to drive")
else:
    print ("You are not allowed to drive")