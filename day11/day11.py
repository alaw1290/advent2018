from tqdm import tqdm

def get_cell_power(cell_x, cell_y, serial_number):
	# formula to calcuate cell power
	# ((((((cell_x + 10) * cell_y) + serial_number) * (cell_x + 10)) // 100) % 10) - 5
	rack_id = cell_x + 10
	power = rack_id * cell_y
	power = power + serial_number
	power = power * rack_id
	power = (power // 100) % 10
	power = power - 5
	return power
	
def get_power_at(cell_x, cell_y, serial_number, square_size=3):
	# get the total power of a grid starting from (cell_x, cell_y)
	power_total = 0
	for y in range(cell_y, cell_y+square_size):
		for x in range(cell_x, cell_x+square_size):
			power_total += get_cell_power(x,y,serial_number)
	return power_total

def find_max_power(grid_size, serial_number, square_size=None):
	
	if square_size:
		power_totals = {}
		for s in tqdm(range(3,square_size)):
			max_power_cell = (0,0)
			max_power_total = -999
			max_power_size = 1
			for x in range(1, grid_size+1):
				for y in range(1, grid_size+1):
					power_total = get_power_at(x, y, serial_number, square_size=s)
					if power_total > max_power_total:
						max_power_total = power_total
						max_power_cell = (x,y)
						max_power_size = s

			power_totals[max_power_total] = max_power_cell, max_power_size
		max_power_cell, max_power_total, max_power_size = sorted([(i,power_totals[i][0], power_totals[i][1]) for i in power_totals])[-1]

	else:
		max_power_cell = (0,0)
		max_power_total = -999
		max_power_size = 3
		for x in range(1, grid_size+1):
			for y in range(1, grid_size+1):
				power_total = get_power_at(x, y, serial_number, square_size=max_power_size)
				if power_total > max_power_total:
					max_power_total = power_total
					max_power_cell = (x,y)
	
	return max_power_cell, max_power_total, max_power_size


def main():

	# test runs #1
	serial_number = 18
	square_size = None
	for j in range(44,49):
		print('\t'.join([str(get_cell_power(i,j,serial_number)) for i in range(32,37)]))
	print(get_power_at(33,45,serial_number, square_size=3))
	print(find_max_power(300, serial_number, square_size=square_size))

	# test runs #2
	serial_number = 42
	square_size = None
	for j in range(60,65):
		print('\t'.join([str(get_cell_power(i,j,serial_number)) for i in range(20,25)]))	
	print(get_power_at(21,61,serial_number, square_size=3))
	print(find_max_power(300, serial_number, square_size=square_size))

	serial_number = 3031
	square_size = None
	print(find_max_power(300, serial_number, square_size=square_size))


	# test runs #3
	serial_number = 3031
	square_size = 50
	print(find_max_power(300, serial_number, square_size=square_size))


		
if __name__ == '__main__':
	main()