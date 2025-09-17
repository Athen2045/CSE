#Parking Registration Scenario
print("Parking Assigner");
trial = 0;
while trial <= 5:
    license = int(input("Enter Your License Number: "));
    checker = license%2
    if checker == 0:
        print("Your License number is Even");
        print("The days you can park are:\n - Monday\n - Wednesday\n - Friday");
        trial+=1
        pass

    elif checker != 0:
        print("Your License number is Odd");
        print("The days you can park are:\n - Tuesday\n - Thursday\n - Saturday");
        trial+=1
        pass

    else: 
        print("Error: Try Again")
        trial+=1
        pass
