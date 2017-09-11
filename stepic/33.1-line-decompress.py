import os
with open('dataset.txt') as input, open('answer.txt', 'w') as output:
	i = 0;
	for line in input:
		while i < len(line) -1:
			symbol = line [i]
			count = line [i+1]
			i +=2
			if (i < len(line)):
				while line[i].isdigit() :
					count = count + line[i]
					i +=1
			part = symbol * int(count)
			output.write(part)
