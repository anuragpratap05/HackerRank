def ransom_note(magazine, rasom):
    c=0
    ans="Yes"
    d = {}
    for word in magazine:
        d.setdefault(word, 0)
        d[word] += 1
        
    #print(d)
    
    for word in rasom:
        if word in d:
            d[word] -= 1
        else:
            c=c+1
            ans="No"
            break
    #print(d)
    
    y= all([x >= 0 for x in d.values()])
    #print(y)
    if ( y==False):
        ans="No"
        
    print(ans)
    
    
m,n=map(int,input().split())
magazine=input().split()
rasom=input().split()
ransom_note(magazine, rasom)
