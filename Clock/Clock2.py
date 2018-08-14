#Условие
#С начала суток часовая стрелка повернулась на угол в α градусов. Определите на какой угол повернулась минутная стрелка
# с начала последнего часа. Входные и выходные данные — действительные числа.

#my solution
angle = float (input())
x = float (90/10800) #коеф. 1 сек = 0.008333333333333333 градус
sec = float (angle/x) #колво секунд прошло
min = float (sec/60) #колво минут прошло
hour = float (min/60) #колво часов прошло
min_after_start = min%60
y = float (180/1800)
angle_min = min_after_start*60*y
print (angle_min)

#Another solution
#angle = float(input())
#print(angle % 30 * 12)