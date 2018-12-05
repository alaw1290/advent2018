# day 1 challenge

def main():
	counter = 0	# running total 
	seen_counters = set()	# current totals seen so far
	solution_1 = None		# the end result of input.txt
	solution_2 = None		# the first repeated value of counter
	while not solution_2:
		with open('input.txt') as file:
			for line in file:
				operator, value = line[0], int(line[1:])	# get the leading operator and delta value
				if operator == "+":
					counter += value
				elif operator == "-":
					counter -= value
				else:
					raise ValueError(f"{operator} input not expected")

				if counter in seen_counters and not solution_2:	# first repeated counter
					solution_2 = counter # store the value of said counter
				else:
					seen_counters.add(counter) # add current counter to seen_counters

		if not solution_1:
			solution_1 = counter	# after first run through input, store the value of counter

	print(f"solution 1: {solution_1}")
	print(f"solution 2: {solution_2}")

if __name__ == '__main__':
	main()