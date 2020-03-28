def average(array):
    x=set(array)
    length=len(x)
    suma=sum(x)
    return suma/length

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
