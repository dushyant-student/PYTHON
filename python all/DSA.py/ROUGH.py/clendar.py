import calendar
while True:
    us=int(input("""1. for calander 
                    2.  for Exit  """))
    if us==1:
        year=int(input("Enter year:- "))
        month =int(input("Enter month:- "))
        cal=calendar.month(year,month)
        print(cal)
    elif us==2:
        break
    else:
        print("invaid input")  #For any integer input
