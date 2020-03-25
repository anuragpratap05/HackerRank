from collections import namedtuple
(n, categories) = (int(input()), input().split())
#print(n,categories)
Grade = namedtuple('Grade', categories)
sum=0
c=0
for i in range (n):
    marks=int(Grade._make(input().split()).MARKS)
    sum=sum+marks;
    c=c+1
x=sum/c
print("{0:.2f}".format(round(x,2)))
