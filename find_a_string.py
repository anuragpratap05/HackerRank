def count_substring(string, sub_string):
    c=0
    x=(len(string)-len(sub_string))
    for i in range(x+1):
        if string[i:i+len(sub_string)]==sub_string:
            c=c+1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
