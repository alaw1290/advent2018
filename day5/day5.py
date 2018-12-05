# day 5 challenge
import string

def breakdown_compound(current_compound, reactions):
	new_compound = "" # new chemical string
	while True:
		new_compound = current_compound # work with copy of current compound
		for val_a, val_b in reactions:
			# replace reactions with empty string
			new_compound = new_compound.replace(val_a + val_b, "") 
			new_compound = new_compound.replace(val_b + val_a, "")
		if current_compound != new_compound:	# continue condition
			current_compound = new_compound
		else:									# end condition
			break
	return new_compound

def main():
	
	current_compound = open("input.txt").read().splitlines()[0].strip() # starting chemical string
	reactions = list(zip(string.ascii_lowercase, string.ascii_uppercase)) # list of reactive pairs
	new_compound = breakdown_compound(current_compound, reactions)
	print(f"final length of input compound: {len(new_compound)}")

	for val_a,val_b in reactions:
		# replace pair with empty string
		test_compound = current_compound
		test_compound = test_compound.replace(val_a, "") 
		test_compound = test_compound.replace(val_b, "")
		test_compound = breakdown_compound(test_compound, reactions)
		print(f"removed vals {val_a,val_b}, final length of compound: {len(test_compound)}")

if __name__ == '__main__':
	main()