#Условие
#Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
#Вклад составляет X рублей Y копеек. Определите размер вклада через год.
#Программа получает на вход целые числа P, X, Y и должна вывести два числа:
# величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.
p = int (input())
x = int (input())
y = int (input())
percent = int((x*100 + y)/100*p)
sum = (x*100 + y) + percent
rub = int (sum//100)
cop = int(sum%100)
print (rub, cop)