def minimumBribes(lst):
    bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)

t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().split()))
    minimumBribes(lst)
