year=int(input("Enter the year\n"))

if((year%400==0) or (year%4==0 and  year%100 !=0)):
    print("leap")
else:
    print("not leap")