def number(n):
    if(n==0):
        return 0
    else:
        return n+number(n-1)
last = number(4)
print(last)