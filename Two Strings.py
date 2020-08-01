n=int(input())
for i in range(n):
    s1=input()
    s2=input()
    s1=set(s1)
    s2=set(s2)
    y=s1.intersection(s2)
    if len(y)>0:
        print("YES")
    else:
        print("NO")
