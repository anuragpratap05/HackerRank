def minion_game(s):
    from collections import Counter
    x=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            x.append(s[i:j])
    z=dict(Counter(x))
    n=(len(z))
    l1=list(z.keys())
    l2=list(z.values())

    q=0
    c=0
    for i in range(len(l1)):
        if l1[i][0] in ['A','E','I','O','U']:
            c=c+l2[i]
        else:
            q=q+l2[i]
    if c>q:
        print("Kevin",c)
    if q>c:
        print("Stuart",q)


    


if __name__ == '__main__':
    s = input()
    minion_game(s)
