x = input("")
y = x.find(" ")
a = x[:y]
b = x[y+1:]
print(b + " " + a)