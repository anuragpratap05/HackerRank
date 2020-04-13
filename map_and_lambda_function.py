cube = lambda x: x**3

def fibonacci(n):
    if(n==0):
        return []
    if(n==1):
        return [0]
    else:
    
        no1=0
        no2=1
        lst=[0,1]
        for i in range(n-2):
            ans=no1+no2
            no1=no2
            no2=ans
            lst.append(ans)
        return lst
    


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
