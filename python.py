marks = float(input("Enter your marks :"))

if marks > 100:
    print("Invalid grade")

elif marks >= 75 and marks < 99:
    print("Your grade is : A")

elif marks >= 65 and marks < 74:
    print("Your grade is : B")

elif marks >= 54 and marks < 65:
    print("Your grade is : C")

elif marks >= 40 and marks < 54:
    print("Your grade is : D")

elif marks >=0 and marks < 39:
    print("Your grade is : F")

else:
    print("Grade invalid")
    