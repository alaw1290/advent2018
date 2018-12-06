# day 3 challenge
from collections import defaultdict

def gen_points_from(point, width, height):
	# point: bottom left of the rectangle
	for x in range(point[0], point[0] + width):
		for y in range(point[1], point[1] + height):
			yield (x,y)

def main():

	main_grid = defaultdict(list) 
	with open('input.txt', 'r') as file:
		for line in file:
			line = line.split(' ')
			rec_id = line[0]
			point = [int(i) for i in line[2].replace(':','').split(',')]
			width, height = [int(i) for i in line[3].split('x')]
			for gen_point in gen_points_from(point, width, height):
				main_grid[gen_point].append(rec_id)


	print(f"points with two or more claims: {len([i for i in main_grid if len(main_grid[i]) > 1])}")

	all_ids = set([i for j in main_grid for i in main_grid[j]])
	bad_ids = set([i for j in main_grid for i in main_grid[j] if len(main_grid[j]) > 1])

	good_ids = all_ids - bad_ids
	print(f"ids with no intersecting claims: {good_ids}")


if __name__ == '__main__':
	main()