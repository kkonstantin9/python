import sys
numbers = {}
max_count = int(sys.stdin.readline())

for i in range(max_count):
    number = int(sys.stdin.readline())
    
    if number in numbers:
      print(numbers[number])
      
    else:
      f_number = f(number)
      print (f_number)
      numbers[number]=f_number
