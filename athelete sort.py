from operator import itemgetter
N, M = map(int, input().split())
lst=[]
for i in range(N):
    x=list(map(int,input().split()))
    lst.append(x)

k=int(input())
ans=sorted(lst, key=itemgetter(k))
for i in ans:
    print(*i)
