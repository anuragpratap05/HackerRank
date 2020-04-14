import re
s=input()
p = re.compile('\w') 
y=(p.findall(s))
ans=("-1")
for i in range(len(y)-1):
    if(y[i]==y[i+1] and y[i]!='_'):
        ans=(y[i])
        break
print(ans)
  
