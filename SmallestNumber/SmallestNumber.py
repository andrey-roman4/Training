a = int (input())
b = int (input())
c = int (input())
if a<=b and a<=c:
    print(a)
else:
    if b<=a and b<=c:
        print(b)
    else:
        if c<=a and c<=b:
            print(c)