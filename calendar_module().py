import calendar
month,day,year=input().split()
x=calendar.weekday(int(year), int(month), int(day))
#print(x)
if(x==0):
    print('MONDAY')
if(x==1):
    print('TUESDAY')
if(x==2):
    print("WEDNESDAY")
if(x==3):
    print("THURSDAY")
if(x==4):
    print("FRIDAY")
if(x==5):
    print("SATURDAY")
if(x==6):
    print("SUNDAY")
