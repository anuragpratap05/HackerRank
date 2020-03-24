from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1)

for j in range(m):
    x=input()
    if(x not in d):
        print("-1")
    else:
        print(*d[x])
    
