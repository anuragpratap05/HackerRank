# HackerRank
HackerRank learning python, since infosys has arrived.....
import re 
n=int(input())
for i in range(n):
    s=input()
    y=(re.sub(r' &&(?= )', ' and' , s, flags = re.IGNORECASE))
    z=(re.sub(r' \|\|(?= )', ' or' , y, flags = re.IGNORECASE))
    print(z)
