t=int(input())
for i in range(t):
    
    r=int(input())
    n=int(input())
    lst=list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n,1):
            x=lst[i]+lst[j]
            if(x==r):
                print(i+1,j+1)
                break
        

