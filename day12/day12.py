# day 12 challenge

# every sequence represented by bitstring
# 32 (5^2) possible rules
from tqdm import tqdm

def reformat(current_state):
	# print it so it looks nice
	return current_state.replace('0','.').replace('1','#')
	# return current_state

def generate_state(current_state, rules):
	new_state = []
	divider_index = current_state.index('|')
	current_state = current_state.replace('|','')
	# search space around current state
	for index in range(-2, len(current_state) + 2): 
		if index == divider_index:
			new_state.append('|')
		if index < 0:
			# searching space before start
			ll = '0'
			l = '0'
			c = '0'
			r = current_state[index + 1] 	if index + 1 >= 0 else '0'
			rr = current_state[index + 2] 	if index + 2 >= 0 else '0'
		elif index >= len(current_state):
			# searching space after end
			ll = current_state[index - 2] 	if index - 2 < len(current_state) else '0'
			l =  current_state[index - 1] 	if index - 1 < len(current_state) else '0'
			c = '0'
			r = '0'
			rr = '0'
		else:
			ll = current_state[index - 2] 	if index - 2 >= 0 else '0'
			l = current_state[index - 1] 	if index - 1 >= 0 else '0'
			c = current_state[index]
			r = current_state[index + 1] 	if index + 1 < len(current_state) else '0'
			rr = current_state[index + 2] 	if index + 2 < len(current_state) else '0'
		try:
			new_state.append(rules[int(ll + l + c + r + rr, 2)])
		except KeyError as E:
			new_state.append('0')

	return ''.join(new_state).strip('0')

def main():
	init_state = ""
	rules = {}
	with open('input.txt', 'r') as file:
		for line in file:
			line = line.strip()
			if 'initial state' in line:
				line = line.split(' ')
				init_state = '|' + line[2].replace('.','0').replace('#','1')
			elif '=>' in line:
				line = line.split (' => ')
				rules_key = int(line[0].replace('.','0').replace('#','1'),2)
				rules_val = '1' if line[1] == '#' else '0'
				rules[rules_key] = rules_val

	# part 1: find sum after 20 iterations
	# print(reformat(init_state))
	new_state = init_state
	for i in tqdm(range(20)):
		new_state = generate_state(new_state, rules)
		# print(reformat(new_state))
	negative, positive = [list(i) for i in new_state.split('|')]
	negative.reverse()
	negative = [i+1 for (i,j) in enumerate(negative) if j == '1']
	positive = [i for (i,j) in enumerate(positive) if j == '1']
	print(sum(positive) - sum(negative))

	# part 2: wait until steady state, then calculate pattern from there
	# print(reformat(init_state))
	new_state = init_state
	remaining_iters = 50000000000
	previous_sum = 0
	previous_delta = 0
	for i in tqdm(range(1,remaining_iters)):
		new_state = generate_state(new_state, rules)
		negative, positive = [list(i) for i in new_state.split('|')]
		negative.reverse()
		negative = [i+1 for (i,j) in enumerate(negative) if j == '1']
		positive = [i for (i,j) in enumerate(positive) if j == '1']
		new_sum = sum(positive) - sum(negative)
		new_delta = new_sum - previous_sum
		if new_delta == previous_delta:
			break
		else:
			previous_sum = new_sum
			previous_delta = new_delta

	# steady state at iteration i
	print(i)
	# current sum
	print(previous_sum)
	# delta for every iteration after i
	print(previous_delta)

	print(previous_sum + ((remaining_iters - i + 1) * previous_delta))

if __name__ == '__main__':
	main()