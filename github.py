n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(n-1):
        if lst[j]<lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
            c=c+1
print(lst)
