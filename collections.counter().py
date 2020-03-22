n=int(input())
s=list(map(int,input().split()))
m=int(input())
sum=0
for i in range(m):
    x,y=input().split()
    for j in range(len(s)):
        if(int(x)==s[j]):
            s.remove(s[j])
            sum=sum+int(y)
            #print(s)
            break
print(sum)

    
