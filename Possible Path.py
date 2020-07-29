import math
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    g1=math.gcd(a,b)
    g2=math.gcd(x,y)
    if(g1==g2):
        print("YES")
    else:
        print("NO")
