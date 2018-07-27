a = int (input ())
b = int (input ())
c = int (input ())
d = int (input ())
x = str
y = str
if a%2 != 0 and b%2 !=0:
    x ='white'
elif a%2 !=0 and b%2 ==0:
    x ='black'
elif a%2 ==0 and b%2 !=0:
    x ='black'
elif a%2 ==0 and b%2 ==0:
    x ='white'
if c%2 != 0 and d%2 !=0:
    y ='white'
elif c%2 !=0 and d%2 ==0:
    y ='black'
elif c%2 ==0 and d%2 !=0:
    y ='black'
elif c%2 ==0 and d%2 ==0:
    y ='white'
if x==y:
    print ('YES')
if x !=y:
    print ('NO')