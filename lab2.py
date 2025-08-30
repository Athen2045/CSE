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


''' fStep 1: Start
Step 2: Display a welcome message
    → Print "Hi!! Welcome to Simple Interest Calculator"
Step 3: Input the principal amount
    → Prompt user to enter the principal amount
    → Store input as prc (float)
Step 4: Input the rate of interest
    → Prompt user to enter the rate (%)
    → Store input as rat (float)
Step 5: Input the time period in months
    → Prompt user to enter time in months
    → Store input as tim (float)
Step 6: Calculate simple interest using the formula
    → simpl = (prc * rat * tim) / 100
Step 7: Round the result to two decimal places
    → interest = round(simpl, 2)
Step 8: Display the calculated simple interest
    → Print "Simple Interest: ", interest
Step 9: End 


### Step 1: Start 
Step 2: Display a welcome message
    → Print "Welcome! Temperature Conversion from C to F"
Step 3: Input temperature in Celsius 
    → Prompt user to enter the Celsius value
    → Store input as cel (float)
Step 4: Convert Celsius to Fahrenheit using the formula
    → fah = (cel × 9/5) + 32
Step 5: Display the result in Fahrenheit
    → Print "Temp in Fahrenheit", fah
Step 6: End


Step 1: Start
Step 2: Display a welcome message
    → Print "Welcome! Temperature Conversion from C to F"
Step 3: Input temperature in Celsius
    → Prompt user to enter the Celsius value
    → Store input as cel (float)
Step 4: Convert Celsius to Fahrenheit using the formula
    → fah = (cel × 9/5) + 32
Step 5: Display the result in Fahrenheit
    → Print "Temp in Fahrenheit", fah
Step 6: End
'''  
