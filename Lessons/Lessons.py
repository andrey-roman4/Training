from math import *
x = int (input())
y = float ((x -1) /2)
a = ceil(y)
b = floor(y)
t = int ((x * 45) + (a * 5) + (b * 15))
h = int (9 + t//60)
m = int (t%60)
print (h,m)

#Условие
#В некоторой школе занятия начинаются в 9:00. Продолжительность урока — 45 минут,
# после 1-го, 3-го, 5-го и т.д. уроков перемена 5 минут,
# а после 2-го, 4-го, 6-го и т.д. — 15 минут.
#Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.
#Выведите два целых числа: время окончания урока в часах и минутах.