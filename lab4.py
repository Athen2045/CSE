#1.Input a number and check:
#- positive
#- Negative
#- Zero

#2. Read marks of a student and print grades:
# - 90 & above -> Grade A
# - 75 to 89 -> Grade B
# - 50 to 74 -> Grade C
# - Below 50 -> Fail

#3. Enter the day number (1-7). Display the corresponding weekday

#4. input electricity units consumed, 
# - 100 -> $2 per unit
# - 101 - 200 -> $5 per unit 
# - above 200 -> $10 per unit 


print("Things to try today");
print('1.Input a number and check');
print('2.Read marks of a student and print grades');
print('3.Enter the day number (1-7)');
print('4.Electricity Bill');
opt=int(input("Enter option:"));

if opt == 1:
    print("***Input a number and check***");
    num=int(input("Enter any number (positive or negative):"));
    if num < 0:
        print("Negative number");

    elif num == 0:
        print("Zero");

    elif num > 0:
        print("Positive number");
    else:
        print("Try again");
    pass

elif opt == 2:
    print("***Read marks of a student and print grades***");
    total=float(input("Enter your total marks (Out of 500):"));
    pr=(total/500)*100;
    pre=round(pr,2);
    
    if pre >= 90:
        print("Grade: A");
    elif pre >= 75 and pre < 90:
        print("Grade: B");
    elif pre >= 50 and pre < 75:
        print("Grade: C");
    else:
        print("Fail");
    pass

elif opt == 3:
    print("***Enter the day number (1-7)***");
    day=int(input("Enter a day number (1 - 7):"));
    if day == 1:
        print("Sunday");

    elif day == 2:
        print("Monday");

    elif day == 3:
        print("Tuesday");

    elif day == 4:
        print("Wednesday");

    elif day == 5:
        print("Thursday");

    elif day == 6:
        print("Friday");

    elif day == 7:
        print("Saturday");
    else:
        print("Try again");
    pass

elif opt == 4:
    print("***Electricity Bill***");
    unit=float(input("Enter units consumed:"));
    
    if unit <= 100:
        bill = unit*2 
        print("Your total bill amount: $", bill);
        
    elif unit >= 101 and unit <= 200:
        bill = unit*5
        print("Your total bill amount: $", bill);
        
    elif unit > 200:
        bill = unit*10 
        print("Your total bill amount: $", bill);
    else:
        print("Enter your units again");
    pass
else:
    print("Wrong Option");
