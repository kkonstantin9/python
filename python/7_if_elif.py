Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.
Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
Обратите внимание, что на вход программе приходят вещественные числа.
Sample Input 1:
5.0
0.0
mod
Sample Output 1:
Деление на 0!
Sample Input 2:
-12.0
-8.0
*
Sample Output 2:
96.0
Sample Input 3:
5.0
10.0
/
Sample Output 3: 
0.5

# put your python code here
A = float (input())
B = float (input())
C = str (input())
if C =='+':
    print(A+B)
elif C=='-':
    print(A-B)
elif C=='*':
    print(A*B)
elif C=='/' and B==0:
    print("Деление на 0!")
elif C=='/' and B!=0:
    print(A/B)
elif C=='mod' and B==0:
    print('Деление на 0!')
elif C=='mod' and B!=0:
    print(A%B)
elif C=='pow':
    print(A**B)
elif C=='div' and B==0:
    print('Деление на 0!')
elif C=='div' and B!=0:
    print(A//B)