#Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, #пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
#Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
#В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.
#Sample Input:
#1
#-3
#5
#-6
#-10
#13
#4
#-8
#Sample Output:
#340
#First version:
b = 1
c = 0
d = 0
while True:
    b = int(input())
    c += b
    d += b ** 2
    if c != 0:
        continue
    else:
        break
print (d)    
#Second version:
a = []
b = 1
c = 0
d = 0
while True:
    b = int(input())
    c += b
    a.append(b)
    if c != 0:
        continue
    else:
        break
for z in a:
    d += z **2
print (d)
