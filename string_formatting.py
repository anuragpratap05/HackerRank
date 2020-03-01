def print_formatted(number):
    w=len(bin(n)[2:])
    for i in range(1,n+1):
         print(str(i).rjust(w,' '),str(oct(i)[2:]).rjust(w,' '),hex(i).lstrip("0x").rstrip("L").upper().rjust(w,' '),bin(i).replace("0b", "").rjust(w,' '))



if __name__ == '__main__':
    n= int(input())
    print_formatted(n)
