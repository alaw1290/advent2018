# day 13 challenge
# assumptions: 
	# all tracks are in loops (each "/" will have a corresponding "\")
	# intersections are all "+" (no three ways)
	# loops can be represented in 1D (0th index is the top left corner of a loop)
	# intersections can be represented as a point along the 1D loop (linking to one other loop)
import re

def cart_path_generator(cart_coordinate, cart_direction, tracks, intersections):
	pass

def main():
	# loops_segements structure: {(y1,y2): x1}
	# end of a loop will be (y2,y1) to a (y1,y2)
	loop_segments = {}
	# loops structure: [((y1,y2),(x1,x2))]
	# can be duplicates of (y1,y2) or (x1,x2)
	loops = []
	# carts structure: {(y,x):dir}
	# dir: ["N"E"S"W"]
	carts = {}
	# intersections structure = [(y,x)]
	intersections = []
	# check if all tracks are loops
	# then store in loop_segments
	with open('input_sample.txt','r') as file:
		for x,line in enumerate(file):
			corner_1 = 	[p.start() for p in re.finditer('/', line)]
			corner_2 = 	[p.start() for p in re.finditer(r'\\', line)]
			n_carts = 	[p.start() for p in re.finditer('\^', line)]
			s_carts = 	[p.start() for p in re.finditer('v', line)]
			e_carts = 	[p.start() for p in re.finditer('>', line)]
			w_carts = 	[p.start() for p in re.finditer('<', line)]
			intersect = [p.start() for p in re.finditer('\+', line)]

			# assert that the number of left/right corners are equal
			assert len(corner_1) == len(corner_2)
			# assert that there aren't any overlapping tracks from corner pairs
			assert all([i[0] > i[1] for i in zip(corner_1[1:],corner_2[:-1])])

			# assemble any loops found
			for segment_1,segment_2 in zip(corner_1, corner_2):
				if (segment_2,segment_1) in loop_segments:
					x1 = loop_segments[(segment_2,segment_1)]
					del loop_segments[(segment_2,segment_1)]
					loops.append(((segment_2,segment_1),(x1,x)))
				else:
					loop_segments[(segment_1,segment_2)] = x

			# add carts 
			for carts_line,direct in [(n_carts, 'N'),(s_carts, 'S'),(e_carts, 'E'),(w_carts, 'W')]:
				for c in carts_line:
					carts[(c,x)] = direct

			# add intersections
			intersections.extend([(i,x) for i in intersect])

	print(intersections)
	# build 1D loops with carts and intersections marked
	for cart in carts:
		pass


if __name__ == '__main__':
	main()