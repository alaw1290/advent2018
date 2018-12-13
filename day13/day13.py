# day 13 challenge
# assumptions: 
	# all tracks are in loops (each "/" will have a corresponding "\")
	# intersections are all "+" (no three ways)
	# loops can be represented in 1D (0th index is the top left corner of a loop)
	# intersections can be represented as a point along the 1D loop (linking to one other loop)
import re

def main():

	# check if all tracks are loops
	with open('input.txt','r') as file:
		for line in file:
			line = line.strip()
			corner_1 = [p.start() for p in re.finditer('/', line)]
			corner_2 = [p.start() for p in re.finditer(r'\\', line)]
			# assert that the number of left/right corners are equal
			assert len(corner_1) == len(corner_2)
			# assert that there aren't any overlapping tracks from corner pairs
			assert all([i[0] > i[1] for i in zip(corner_1[1:],corner_2[:-1])])

if __name__ == '__main__':
	main()