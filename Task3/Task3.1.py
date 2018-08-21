import math
#Repaper
z = input("Enter the word: " )
#z = ("Repaper")
z = z.lower()
print(z)
y = len(z)/2
k = int (math.ceil(y))
l = int (math.floor(y))
a = z[:k]
b = z[l:]
h = b[::-1]
print(a)
print(h)
if a==h:
    print ("Palyndrom")
else:
    print ("Not Palyndrom")