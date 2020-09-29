import re

actual_data = open('./regex_sum_996182.txt')
sum_num = 0
for line in actual_data:
	line = line.rstrip()
	y = re.findall('[0-9]+', line)
	if y :
		sum_num += sum(list(map(int,y)))
print(sum_num)