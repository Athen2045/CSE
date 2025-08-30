print("Things to try");
print('1.Simple interest calculator');
print('2.Temp from Celsius to Fahrenheit');
print('3.Temp from Fahrenheit to Celsius');
opt=int(input("Enter option:"));
if opt == 1:
    print("Hi!!\n Welcome to Simple Interest Calculator");
    prc=float(input("Enter Principle amount:"));
    rat=float(input("Enter Rate%:"));
    tim=float(input("Enter Time (In Months):"));
    simpl=(prc*rat*tim)/100;
    interest=round(simpl,2);
    print("Simple Interest:",interest);

elif opt == 2:
    print("***Welcome!\nTemperature Conversion from C to F***");
    cel=float(input("Enter the Celsius:"));
    fah=(cel*9/5) + 32;
    print("Temp in Fahrenheit", fah);

elif opt == 3:
    print("***Welcome!\nTemperature Conversion from F to C***");
    fah=float(input("Enter the Fahrenheit:"));
    cel=(fah-32)*(5/9);
    print("Temp in Celsius", cel);
else:
    print("Wrong Option");
