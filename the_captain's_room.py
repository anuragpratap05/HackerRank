n=int(input())
s=list(map(int,input().split()))
add=sum(s)
y=list(set(s))
#print(y)
temp=sum(y)*n
for i in y:
    ans=temp-(i*(n-1))
    if(ans==add):
        print(i)
        break
