# day 2 challenge
from collections import Counter
import string
import numpy as np

def vectorize(line):
	return np.array([string.ascii_lowercase.index(c) for c in line])

def compare_vectors(vector, line_vectors):
	for line,vec in line_vectors:
		if np.sum(vector != vec) == 1:
			return line
	return False

def main():
	count_2_letters = 0 # number of lines with a char that repeats exactly 2 times
	count_3_letters = 0 # number of lines with a char that repeats exactly 3 times
	line_vectors = [] 	# lines with vectorized lines 
	matched_ids = None	# matched IDs
	with open('input.txt') as file:
		for line in file:
			line_id = line.strip()
			line_letter_counter = Counter(line_id) 	# convert line into counter
			if any([line_letter_counter[letter] == 2 for letter in line_letter_counter]): # there exists a char that repeat 2 times
				count_2_letters += 1
			if any([line_letter_counter[letter] == 3 for letter in line_letter_counter]): # there exists a char that repeat 3 times
				count_3_letters += 1

			vector = vectorize(line_id)	# vectorize line 
			matched_id = compare_vectors(vector, line_vectors)
			if matched_id:
				matched_ids = [line_id, matched_id]
			else:
				line_vectors.append((line_id,vector))


	print(f"checksum 1: {count_2_letters*count_3_letters}")
	print(f"matching ids: {matched_ids}")

if __name__ == '__main__':
	main()