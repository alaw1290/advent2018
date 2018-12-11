# day 4 challenge
from datetime import datetime
from collections import defaultdict

def main():

	input_data = {}
	with open('input_sample.txt','r') as file:
		for line in file:
			line = line.strip()
			timestamp = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')
			update = line[25:28]
			if update == 'asl':
				update = False
			elif update == 'up':
				update = True
			else:
				update = int(update[1:])
				guards.add(update)
			input_data.append((timestamp,update))

	input_data = sorted(input_data)
	guard = input_data[0][1]
	previous_awake_time = input_data[0][0]
	print(previous_awake_time, guard)
	guard_schedule = {guard:[]}
	for timestamp,update in input_data:
		if isinstance(update,int):


if __name__ == '__main__':
	main()