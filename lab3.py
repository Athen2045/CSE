#Q.1 A student enters their age. If the age is 18 or above, display "Ëligible to vote"
#Q.2 Read a number from the user. If it is even, print "Even number"
#Q.3 Enter temperature in  *C. If it is greater than 30, display "it is a hot day'
#Q.4 Read marks of a student. If marks are 90 or above, display "Grade A+"


print("Things to try");
print('1.Vote Eligibilty');
print('2.Even or Odd');
print('3.Temperature System');
print('4.Marks System');
opt=int(input("Enter option:"));
if opt == 1:
    print("Vote Eligibility");
    age=int(input("Enter your age:"));
    if age >= 18:
        print("Eligible to Vote");
    else:
        print("Not Eligible");
    pass

elif opt == 2:
    print("Even or Odd?");
    num=float(input("Enter a number:"));
    even = num % 2;
    if even == 0:
        print("Even number");
    else:
        print("Odd number");
    pass

elif opt == 3:
    print("Temperature System");
    temp=float(input("Enter the current temperature in *C:"));
    if temp >= 30:
        print("It is a hot day");
    else:
        print("It is a cool day");
    pass

elif opt == 4:
    print("***Mark sheet system***");
    sub1=float(input("Enter Math Marks (Out of 100):"));
    sub2=float(input("Enter Phy Marks (Out of 100):"));
    sub3=float(input("Enter Chem Marks (Out of 100):"));
    sub4=float(input("Enter Eng Marks (Out of 100):"));
    total=sub1+sub2+sub3+sub4;
    pr=(total/400)*100;
    pre=round(pr,2);
    
    if pre >= 90:
        print("Grade: A+");
    elif pre >= 85 and pre < 90:
        print("Grade: A");
    elif pre >= 70 and pre < 85:
        print("Grade: B");
    elif pre >= 60 and pre < 70:
        print("Grade: C");
    else:
        print("Grade: D");
    pass
else:
    print("Wrong Option");

