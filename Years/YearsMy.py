x = int(input())
if x%400 ==0 and x%100 ==0 and x%4 ==0:
    print('YES')
else:
    if x%400 !=0 and x%100 ==0 and x%4 ==0:
        print('NO')
    else:
        if x%400 !=0 and x%100 !=0 and x%4 ==0:
            print('YES')
        else:
            if x%400 !=0 and x%100 !=0 and x%4 !=0:
                print('NO')