# HackerRank
HackerRank learning python, since infosys has arrived.....
import re
t=int(input())
for i in range(t):
    if re.match(r'[789]\d{9}$',input()):   
       print("YES")
    else:
        print("NO")
      
