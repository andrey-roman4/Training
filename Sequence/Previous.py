#Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности больше предыдущего элемента.
x = int
previous = 0
count = -1
while x !=0:
    x = int (input())
    if x > previous:
        count +=1
        previous = x
    else:
        previous = x
print (count)