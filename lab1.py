print("Things to try");
print('1.Marks system');
print('2.Area & Perimeter of square');
print('3.Area of circle');
opt=int(input("Enter option:"));
if opt == 1:
    print("***Mark sheet system***");
    sub1=float(input("Enter Math Marks (Out of 100):"));
    sub2=float(input("Enter Phy Marks (Out of 100):"));
    sub3=float(input("Enter Chem Marks (Out of 100):"));
    sub4=float(input("Enter Eng Marks (Out of 100):"));
    total=sub1+sub2+sub3+sub4;
    pr=(total/400)*100;
    pre=round(pr,2);
    print("Total marks:",total);
    print("Total %:",pre);
    
    if pre >= 85:
        print("Grade: A");
    elif pre >= 70 and pre < 85:
        print("Grade: B");
    elif pre >= 60 and pre < 70:
        print("Grade: C");
    else:
        print("Grade: D");
    pass

elif opt == 2:
    print("***Area & Perimeter of rectangle***");
    l=float(input("Enter the length of rectangle:"));
    b=float(input("Enter the breadth of rectangle:"));
    area=l*b;
    peri=(2*l)+(2*b);
    print("The Area of the rectangle:", area);
    print("The Perimeter of the rectangle:", peri);

elif opt == 3:
    print("***Area of Circle***");
    r=float(input("Enter the radius:"));
    a=2*3.14*r*r;
    area=round(a,2);
    print("The Area of circle:", area);
else:
    print("Wrong Option");

