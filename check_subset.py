#t=int(input())
for i in range (t):
    n=int(input())
    A=set(input().split())
    m=int(input())
    B=set(input().split())
    x=(len(A.difference(B)))
    if(x==0):
        print("True")
    else:
        print("False")
        
