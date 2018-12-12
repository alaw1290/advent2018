# day 10 challenge

import re
from collections import Counter
from tqdm import tqdm
import matplotlib.pyplot as plt

def distance(p1, p2):
	return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5


class Star(object):
	def __init__(self, position, velocity):
		self.position = position
		self.velocity = velocity

	def __repr__(self):
		return f"Star@{self.position}"

	def position_at(self, time_step):
		# exact position at time_step 
		delta_x = self.velocity[0]*time_step
		delta_y = self.velocity[1]*time_step
		return (self.position[0] + delta_x, self.position[1] + delta_y)

	def time_at(self, position):
		# find time_step where star is closest to position
		time_step = 0
		min_dist = distance(self.position, position)
		while True:
			time_step += 1
			next_position = self.position_at(time_step)
			dist = distance(next_position, position)
			if dist >= min_dist :
				return time_step-1
			else:
				min_dist = dist



def main():

	stars = []	# track all star positions and velocity vectors 

	with open('input.txt', 'r') as file:
		for line in file:
			data = re.findall('<(.+?)>', line)
			data = [i.split(',') for i in data]
			position = (int(data[0][0]), int(data[0][1]))
			velocity = (int(data[1][0]), int(data[1][1]))
			x = Star(position, velocity)
			stars.append(x)

	for time in tqdm(range(10475,10520)):
		xs = []
		ys = []
		for star in stars:
			x1,y1 = star.position_at(time)
			xs.append(x1)
			ys.append(y1)
		if Counter(xs).most_common(1)[0][1] >= 20:
			plt.scatter(xs,ys)
			plt.show()
			print(time)
		else:
			continue
	plt.show()

	xs = []
	ys = []

	for star in stars:
		x1,y1 = star.position_at(10476)
		xs.append(x1)
		ys.append(y1)
	plt.scatter(xs,ys)
	plt.show()

if __name__ == '__main__':
	main()
