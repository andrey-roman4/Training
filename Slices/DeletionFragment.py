#Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними.
x = input('')
a = x.find('h')
b = x.rfind('h')
x = x[:a] + x[b+1:]
print(x)