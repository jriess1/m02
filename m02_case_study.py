#Joseph riess
#GPATest
#tests whether or not the students GPA is high enough to be on the deans list or if theyre on the honor roll

lastName = input("What is the student's last name? Enter ZZZ to quit.")
while lastName != "ZZZ":
    firstName = input("What is the student's first name?")
    GPA = float(input("What is the student's GPA?"))

    if GPA >= 3.5:
        print(firstName + " " + lastName + " is on the Dean's list.")
    elif GPA >=3.25:
        print(firstName + " " + lastName + " is on the Honor Roll")
    
    lastName = input("What is the student's last name? Enter ZZZ to quit.")
