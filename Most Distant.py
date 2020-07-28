import math as m
n=int(input())
xlst=[]
ylst=[]
ans=0
for i in range(n):
    x,y=map(int,input().split())
    if x==0:
        ylst.append(y)
    else:
        xlst.append(x)
        

#print(xlst)
#print(ylst)        
#xmin=min(xlst)
#xmax=max(xlst)
#ymin=min(ylst)
#ymax=max(ylst)
#print(xmax,xmin)
#print(ymax,ymin)


        
if len(xlst)==0:
    ymin=min(ylst)
    ymax=max(ylst)
    ans=ymax-ymin
    
    
if len(ylst)==0:
    xmin=min(xlst)
    xmax=max(xlst)
    ans=xmax-xmin
    
    
if len(xlst)==1 and len(ylst)==1:
    ans=m.sqrt((xlst[0])**2+(ylst[0])**2)
    
    
if len(xlst)==1 and len(ylst)>=2:
    ymin=min(ylst)
    ymax=max(ylst)
    maxi=ymax-ymin
    diag1=m.sqrt(ymax**2+(xlst[0])**2)
    diag2=m.sqrt(ymin**2+(xlst[0])**2)
    ans=max(maxi,diag1,diag2)
    

if len(ylst)==1 and len(xlst)>=2:
    xmin=min(xlst)
    xmax=max(xlst)
    maxi=xmax-xmin
    diag1=m.sqrt(xmax**2+(ylst[0])**2)
    diag2=m.sqrt(xmin**2+(ylst[0])**2)
    ans=max(maxi,diag1,diag2)


if len(xlst)>=2 and len(ylst)>=2:
    xmin=min(xlst)
    xmax=max(xlst)
    ymin=min(ylst)
    ymax=max(ylst)
    maxi1=xmax-xmin
    maxi2=ymax-ymin
    diag1=m.sqrt(ymax**2+xmax**2)
    diag2=m.sqrt(ymax**2+xmin**2)
    diag3=m.sqrt(ymin**2+xmin**2)
    diag4=m.sqrt(ymin**2+xmax**2)
    ans=max(maxi1,maxi2,diag1,diag2,diag3,diag4)
    
#print(ans)
print("{:.6f}".format(ans));

