#Дана строка, в которой буква h встречается как минимум два раза.
# Разверните последовательность символов, заключенную между первым и
# последним появлением буквы h, в противоположном порядке.
x = input('')
a = x.find('h')
b = x.rfind('h')
c = x[a:b+1]
d = c[::-1]
y = x.replace(c,d)
print(y)