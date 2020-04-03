n,m=map(int,input().split())
lst=[]
for i in range(m):
    x=map(float,input().split())
    
    lst.append(x)
#print(lst)
y=(list(zip(*lst)))
for i in range(n):
    print(sum(y[i])/m)
