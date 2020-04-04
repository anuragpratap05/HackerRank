s=input()
upper=[]
lower=[]
number=[]
odd=[]
even=[]
for i in range(len(s)): 
    if str(s[i]) >= 'A' and str(s[i]) <= 'Z': 
        upper.append(s[i])
    elif str(s[i]) >= 'a' and str(s[i]) <= 'z': 
        lower.append(s[i])
    elif str(s[i]) >= '0' and str(s[i]) <= '9': 
        number.append(s[i])

for i in number:
    if int(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
LOWER=(sorted(lower))
UPPER=(sorted(upper))
ODD=(sorted(odd))
EVEN=(sorted(even))
print("".join(LOWER+UPPER+ODD+EVEN))
         
