r,c=map(int,input().split())
if(r==1):
    x=0
if(r==2):
    x=1
if(r>2 and r%2!=0):
    x=10
    y=r-3
    z=y//2
    x=x+z*10

if(r>3 and r%2==0):
    x=11
    y=r-4
    z=y//2
    x=x+z*10
#print(x)

if(c==1):
    print(x)
if(c==2):
    print(x+2)
if(c==3):
    print(x+4)
if(c==4):
    print(x+6)
if(c==5):
    print(x+8)
