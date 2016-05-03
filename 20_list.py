Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.
Используйте метод split строки.
Sample Input:
4 -1 9 3
Sample Output:
15

#your python code here
a  = [int(i) for i in input().split()]
c = 0
for x in a:
	c += x
print(c)